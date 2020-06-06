import pymel.core as pm


class Rig:
    def __init__(self, root, side="left"):
        self.side = side

        self.result_chain, self.ik_chain, self.fk_chain = \
            self._joint_chains(root, side)

        self.controls = self._controls(
            side, self.result_chain, self.ik_chain, self.fk_chain)

    @staticmethod
    def _joint_chains(root, side):
        result_chain = [root] + root.getChildren(ad=1)[::-1]
        names = ["thigh", "shin", "foot", "ball", "toe"]
        for jnt, name in zip(result_chain, names):
            jnt.rename("{}{}_result_JNT".format(side, name.capitalize()))

        pm.joint(result_chain[0], e=1, oj="xyz", sao="xup", ch=1, zso=1)
        ik_chain = pm.duplicate(result_chain)
        fk_chain = pm.duplicate(result_chain)
        for ik, fk in zip(ik_chain, fk_chain):
            name = ik.replace("result", "IK")
            ik.rename(name)
            name = fk.replace("result", "FK")
            fk.rename(name)
        ik_chain[0].rename(ik_chain[0][:-1])
        fk_chain[0].rename(fk_chain[0][:-1])

        result_dict = {}
        ik_dict = {}
        fk_dict = {}
        for k, r, ik, fk in zip(names, result_chain, ik_chain, fk_chain):
            result_dict[k] = r
            ik_dict[k] = ik
            fk_dict[k] = fk
        return result_dict, ik_dict, fk_dict

    @staticmethod
    def _controls(side, result_chain, ik_chain, fk_chain):
        leg_settings = pm.spaceLocator(n=side+"Leg_settings_CON")
        pm.parentConstraint(result_chain["foot"], leg_settings)
        controls = {"leg_settings": leg_settings}

        thigh_fk = pm.spaceLocator(n=side+"Thigh_FK_CON")
        thigh_fk.rotateOrder.set(3)  # xzy
        pm.matchTransform(thigh_fk, fk_chain["thigh"])
        controls["thigh_fk"] = thigh_fk

        shin_fk = pm.spaceLocator(n=side+"Shin_FK_CON")
        shin_fk.rotateOrder.set(3)
        pm.matchTransform(shin_fk, fk_chain["shin"])
        controls["shin_fk"] = shin_fk

        foot_fk = pm.spaceLocator(n=side+"Foot_FK_CON")
        foot_fk.rotateOrder.set(3)
        pm.matchTransform(foot_fk, fk_chain["foot"])
        controls["foot_fk"] = foot_fk

        ball_fk = pm.spaceLocator(n=side+"Ball_FK_CON")
        ball_fk.rotateOrder.set(3)
        pm.matchTransform(ball_fk, fk_chain["ball"])
        controls["ball_fk"] = ball_fk

        foot_ik = pm.spaceLocator(n=side+"Foot_CON")
        foot_ik.rotateOrder.set(2)
        pm.matchTransform(foot_ik, ik_chain["foot"], pos=1)
        controls["foot_ik"] = foot_ik

        knee_ik = pm.spaceLocator(n=side+"Knee_CON")
        pm.matchTransform(knee_ik, ik_chain["shin"], pos=1)
        knee_ik.tz.set(knee_ik.tz.get() + 10)
        controls["knee_ik"] = knee_ik

        if pm.objExists("settings_GRP"):
            pm.parent(leg_settings, "settings_GRP")
        else:
            pm.group(n="settings_GRP", em=1)
            pm.parent(leg_settings, "settings_GRP")

        for con in controls.values()[1:]:
            grp = pm.duplicate(con, n=con.replace("CON", "OFS"))[0]
            pm.delete(grp.getShapes())
            pm.parent(con, grp)
        return controls

    def ikfk_switch(self):
        leg_settings = self.controls["leg_settings"]
        result_chain, ik_chain, fk_chain = \
            self.result_chain, self.ik_chain, self.fk_chain
        names = ["thigh", "shin", "foot", "ball", "toe"]
        side = self.side

        pm.addAttr(leg_settings,
                   longName="FK_IK_blend",
                   niceName="FK/IK Blend",
                   attributeType="float",
                   keyable=1,
                   minValue=0,
                   maxValue=1)

        nodes = []
        for n in names:
            pair_blend = pm.createNode(
                "pairBlend",
                n="{}{}_IKFKChoice".format(side, n.capitalize()))
            fk_chain[n].rotate >> pair_blend.inRotate1
            ik_chain[n].rotate >> pair_blend.inRotate2
            pair_blend.outRotate >> result_chain[n].rotate

            fk_chain[n].translate >> pair_blend.inTranslate1
            ik_chain[n].translate >> pair_blend.inTranslate2
            pair_blend.outTranslate >> result_chain[n].translate

            leg_settings.FK_IK_blend >> pair_blend.weight
            nodes += [pair_blend]

        #TODO: blend between IK/FK controls and chain
        return nodes

    def fk_leg(self):
        names = ["thigh", "shin", "foot"][::-1]
        ofs = self.controls["ball_fk"].getParent()
        for n in names:
            con = self.controls[n+"_fk"]
            pm.parent(ofs, con)
            ofs = con.getParent()

        controls = []
        for v in self.controls.values():
            if "FK" not in str(v):
                continue
            fk_jnt = v.replace("CON", "JNT")
            pm.parentConstraint(v, fk_jnt)
            controls += [v]

        # SDK setup
        thigh_fk_con = self.controls["thigh_fk"]
        shin_fk_con = self.controls["shin_fk"]
        foot_fk_con = self.controls["foot_fk"]

        pm.addAttr(thigh_fk_con, ln="length", at="float", k=1, min=0, dv=1)
        pm.addAttr(shin_fk_con, ln="length", at="float", k=1, min=0, dv=1)

        # SDK - thigh >> shin
        driven = shin_fk_con.getParent().tx
        driver = thigh_fk_con.length

        pm.setDrivenKeyframe(driven, cd=driver)
        pm.setInfinity(driven, poi="linear")
        pm.setDrivenKeyframe(driven, cd=driver, dv=0, v=0)

        # SDK - shin >> foot
        driven = foot_fk_con.getParent().tx
        driver = shin_fk_con.length

        pm.setDrivenKeyframe(driven, cd=driver)
        pm.setInfinity(driven, poi="linear")
        pm.setDrivenKeyframe(driven, cd=driver, dv=0, v=0)
        return controls

    def ik_leg(self):
        ik_chain = self.ik_chain
        side = self.side
        foot_control = self.controls["foot_ik"]

        # IK HANDLES
        leg_hdl, leg_eff = pm.ikHandle(
            sj=ik_chain["thigh"], ee=ik_chain["foot"], sol="ikRPsolver")
        leg_hdl.rename(side+"Leg_HDL")
        leg_eff.rename(side+"Leg_EFF")
        pm.parent(leg_hdl, foot_control)

        ball_hdl, ball_eff = pm.ikHandle(
            sj=ik_chain["foot"], ee=ik_chain["ball"], sol="ikRPsolver")
        ball_hdl.rename(side+"Ball_HDL")
        ball_eff.rename(side+"Ball_EFF")
        pm.parent(ball_hdl, foot_control)

        toe_hdl, toe_eff = pm.ikHandle(
            sj=ik_chain["ball"], ee=ik_chain["toe"], sol="ikRPsolver")
        toe_hdl.rename(side+"Toe_HDL")
        toe_eff.rename(side+"Toe_EFF")
        pm.parent(toe_hdl, foot_control)

        # SDK for Leg Stretch and Bend
        leg_start_loc = pm.spaceLocator(n=side+"Leg_IK_lengthStart_LOC")
        leg_end_loc = pm.spaceLocator(n=side+"Leg_IK_lengthEnd_LOC")

        pm.matchTransform(leg_start_loc, ik_chain["thigh"], pos=1)
        pm.matchTransform(leg_end_loc, ik_chain["foot"], pos=1)

        leg_length = pm.distanceDimension(
            sp=leg_start_loc.worldPosition.get(),
            ep=leg_end_loc.worldPosition.get())
        leg_length.getParent().rename(side+"Leg_IK_length")

        pm.parent(leg_end_loc, foot_control)

        # --- SDK for thigh
        thigh_length = ik_chain["shin"].tx.get()
        shin_length = ik_chain["foot"].tx.get()
        sum_length = thigh_length + shin_length
        pm.setDrivenKeyframe(
            ik_chain["shin"].tx,
            cd=leg_length.distance,
            dv=sum_length,
            v=thigh_length
        )
        pm.setDrivenKeyframe(
            ik_chain["shin"].tx,
            cd=leg_length.distance,
            dv=sum_length*2,
            v=thigh_length*2
        )
        pm.setInfinity(ik_chain["shin"].tx, poi="linear")

        # --- SDK for shin
        shin_length = ik_chain["foot"].tx.get()
        pm.setDrivenKeyframe(
            ik_chain["foot"].tx,
            cd=leg_length.distance,
            dv=sum_length,
            v=shin_length
        )
        pm.setDrivenKeyframe(
            ik_chain["foot"].tx,
            cd=leg_length.distance,
            dv=sum_length*2,
            v=shin_length*2
        )
        pm.setInfinity(ik_chain["foot"].tx, poi="linear")

        # --- SDK for foot
        foot_length = ik_chain["toe"].tx.get()
        pm.setDrivenKeyframe(
            ik_chain["toe"].tx,
            cd=leg_length.distance,
            dv=sum_length,
            v=foot_length
        )
        pm.setDrivenKeyframe(
            ik_chain["toe"].tx,
            cd=leg_length.distance,
            dv=sum_length*2,
            v=foot_length*2
        )
        pm.setInfinity(ik_chain["toe"].tx, poi="linear")

        # DUAL KNEE SET UP
        knee_control = self.controls["knee_ik"]
        knee_loc = pm.spaceLocator(n=side+"Knee_LOC")
        pm.matchTransform(knee_loc, knee_control)
        pm.poleVectorConstraint(knee_loc, leg_hdl)

        pm.matchTransform(knee_loc, foot_control)
        knee_loc.tx.set(knee_loc.tx.get() + 10)
        leg_hdl.twist.set(90)

        no_flip_group, = pm.duplicate(foot_control, po=1, n=side+"NoFlip_GRP")
        pm.parent(no_flip_group, foot_control)
        pm.parent(knee_loc, no_flip_group)

        pm.addAttr(foot_control, ln="kneeTwist", at="float", k=1)
        foot_control.kneeTwist >> no_flip_group.ry

        # --- no flip knee

        return True

    def cleanup(self):
        # fk controls - lock and hide everything except rotate

        # hide ik handles
        # hide distance nodes
        # lock and hide control offsets
        return
