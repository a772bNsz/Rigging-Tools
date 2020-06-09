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

        pm.addAttr(leg_settings, ln="FK_IK_blend", nn="FK/IK Blend",
                   at="float", k=1, min=0, max=1)

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

        pm.addAttr(leg_settings, ln="IK_visibility", at="bool", k=0, h=1)
        pm.addAttr(leg_settings, ln="FK_visibility", at="bool", k=0, h=1)
        pm.addAttr(leg_settings, ln="knee_visibility", at="bool", k=0, h=1)

        leg_settings.FK_visibility >> self.controls["thigh_fk"].getParent().v
        leg_settings.IK_visibility >> self.controls["foot_ik"].getParent().v
        leg_settings.knee_visibility >> self.controls["knee_ik"].v

        pm.setDrivenKeyframe(leg_settings.FK_visibility,
                             cd=leg_settings.FK_IK_blend, dv=0, v=1)
        pm.setDrivenKeyframe(leg_settings.FK_visibility,
                             cd=leg_settings.FK_IK_blend, dv=0.999, v=1,
                             itt="linear", ott="linear")
        pm.setDrivenKeyframe(leg_settings.FK_visibility,
                             cd=leg_settings.FK_IK_blend, dv=1, v=0)

        pm.setDrivenKeyframe(leg_settings.IK_visibility,
                             cd=leg_settings.FK_IK_blend, dv=0, v=0)
        pm.setDrivenKeyframe(leg_settings.IK_visibility,
                             cd=leg_settings.FK_IK_blend, dv=0.001, v=1,
                             itt="linear", ott="linear")
        pm.setDrivenKeyframe(leg_settings.IK_visibility,
                             cd=leg_settings.FK_IK_blend, dv=1, v=1)

        pm.setDrivenKeyframe(self.controls["knee_ik"].getParent().v,
                             cd=leg_settings.FK_IK_blend, dv=0, v=0)
        pm.setDrivenKeyframe(self.controls["knee_ik"].getParent().v,
                             cd=leg_settings.FK_IK_blend, dv=0.001, v=1,
                             itt="linear", ott="linear")
        pm.setDrivenKeyframe(self.controls["knee_ik"].getParent().v,
                             cd=leg_settings.FK_IK_blend, dv=1, v=1)
        return nodes

    def fk_leg(self):
        names = ["thigh", "shin", "foot"][::-1]
        ofs = self.controls["ball_fk"].getParent()
        for n in names:
            con = self.controls[n+"_fk"]
            pm.parent(ofs, con)
            ofs = con.getParent()

        for v in self.controls.values():
            if "FK" not in str(v):
                continue
            fk_jnt = v.replace("CON", "JNT")
            pm.parentConstraint(v, fk_jnt)

        # SDK setup
        thigh_fk_con = self.controls["thigh_fk"]
        shin_fk_con = self.controls["shin_fk"]
        foot_fk_con = self.controls["foot_fk"]

        pm.addAttr(thigh_fk_con, ln="length", at="float", k=1, min=0, dv=1)
        pm.addAttr(shin_fk_con, ln="length", at="float", k=1, min=0, dv=1)

        # --- SDK - thigh >> shin
        driven = shin_fk_con.getParent().tx
        driver = thigh_fk_con.length

        pm.setDrivenKeyframe(driven, cd=driver)
        pm.setInfinity(driven, poi="linear")
        pm.setDrivenKeyframe(driven, cd=driver, dv=0, v=0)

        # --- SDK - shin >> foot
        driven = foot_fk_con.getParent().tx
        driver = shin_fk_con.length

        pm.setDrivenKeyframe(driven, cd=driver)
        pm.setInfinity(driven, poi="linear")
        pm.setDrivenKeyframe(driven, cd=driver, dv=0, v=0)

        # Controls
        controls = {
            "thigh": thigh_fk_con,
            "shin": shin_fk_con,
            "foot": foot_fk_con
        }
        return controls

    def ik_leg(self):
        # Dual Knee
        no_flip_chain = self._dual_knee("noFlip")
        pv_chain = self._dual_knee("pv")
        self._dual_knee_switch(no_flip_chain, pv_chain)

        # IK Foot Handles on IK Chain
        ik_chain = self.ik_chain
        side = self.side
        foot_control = self.controls["foot_ik"]

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

        # Controls
        controls = {
            "foot": foot_control,
            "knee": self.controls["knee_ik"]
        }
        return controls

    def _dual_knee(self, knee_type):
        # Basic IK Leg
        dup_ik_chain = self._basic_ik_leg(knee_type)
        leg_hdl = dup_ik_chain["thigh"].outputs(type="ikHandle")[0]

        # IK Stretch and Bend
        self._ik_stretch(knee_type, dup_ik_chain)

        # Automatic or Manual Knee >> _noflip_knee() or _pv_knee()
        knee_control = self.controls["knee_ik"]
        side = self.side
        knee_loc = pm.spaceLocator(n="{}Knee_{}_LOC".format(side, knee_type))
        pm.matchTransform(knee_loc, knee_control)
        pm.poleVectorConstraint(knee_loc, leg_hdl)

        knee_method = "_{}_knee".format(knee_type.lower())
        getattr(self, knee_method)(knee_loc, dup_ik_chain)
        return dup_ik_chain

    def _basic_ik_leg(self, knee_type):
        foot_control = self.controls["foot_ik"]
        side = self.side

        # Duplicate IK Chain
        ik_chain = {}
        dup_chain = pm.duplicate(self.ik_chain["thigh"])
        dup_chain += dup_chain[0].getChildren(ad=1)[::-1]
        pm.delete(dup_chain.pop(), dup_chain.pop())
        for k, jnt in zip(["thigh", "shin", "foot"], dup_chain):
            n = jnt.replace("IK", knee_type+"_IK")
            n = n[:-1] if jnt.endswith("1") else n
            jnt.rename(n)
            ik_chain[k] = jnt

        # IK Handles
        leg_hdl, leg_eff = pm.ikHandle(
            sj=ik_chain["thigh"],
            ee=ik_chain["foot"],
            sol="ikRPsolver")
        leg_hdl.rename("{}Leg_{}_HDL".format(side, knee_type))
        leg_eff.rename("{}Leg_{}_EFF".format(side, knee_type))
        pm.parent(leg_hdl, foot_control)
        return ik_chain
    
    def _ik_stretch(self, knee_type, ik_chain):
        # SDK for Leg Stretch and Bend
        foot_control = self.controls["foot_ik"]
        side = self.side
        
        leg_start_loc = pm.spaceLocator(
            n="{}Leg_{}_IK_lengthStart_LOC".format(side, knee_type))
        leg_end_loc = pm.spaceLocator(
            n="{}Leg_{}_IK_lengthEnd_LOC".format(side, knee_type))

        pm.matchTransform(leg_start_loc, ik_chain["thigh"], pos=1)
        pm.matchTransform(leg_end_loc, ik_chain["foot"], pos=1)

        leg_length = pm.distanceDimension(
            sp=leg_start_loc.worldPosition.get(),
            ep=leg_end_loc.worldPosition.get()).getParent()
        leg_length.rename("{}Leg_{}_IK_length".format(side, knee_type))

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
        return
    
    def _noflip_knee(self, knee_loc, ik_chain):
        foot_control = self.controls["foot_ik"]
        side = self.side
        leg_hdl = ik_chain["thigh"].outputs(type="ikHandle")[0]

        pm.matchTransform(knee_loc, foot_control)
        knee_loc.tx.set(knee_loc.tx.get() + 10)
        leg_hdl.twist.set(90)

        no_flip_group, = pm.duplicate(
            foot_control, po=1, n=side+"NoFlip_GRP")
        pm.parent(no_flip_group, foot_control)
        pm.parent(knee_loc, no_flip_group)

        pm.addAttr(foot_control, ln="kneeTwist", at="float", k=1)
        foot_control.kneeTwist >> no_flip_group.ry

        # Non-uniform IK Leg Stretch
        pm.addAttr(foot_control,
                   ln="autoKneeThighLength", at="float", k=1, min=0, dv=1)
        pm.addAttr(foot_control,
                   ln="autoKneeShinLength", at="float", k=1, min=0, dv=1)

        shin_sdk = ik_chain["shin"].tx.inputs()[0]
        foot_sdk = ik_chain["foot"].tx.inputs()[0]

        knee_stretch = \
            pm.createNode("multiplyDivide", n=side+"Knee_noFlipScale_MULT")

        foot_control.autoKneeThighLength >> knee_stretch.input1X
        shin_sdk.output >> knee_stretch.input2X
        knee_stretch.outputX >> ik_chain["shin"].tx

        foot_control.autoKneeShinLength >> knee_stretch.input1Y
        foot_sdk.output >> knee_stretch.input2Y
        knee_stretch.outputY >> ik_chain["foot"].tx
        return
    
    def _pv_knee(self, knee_loc, ik_chain):
        knee_control = self.controls["knee_ik"]
        foot_control = self.controls["foot_ik"]
        side = self.side
        
        pm.parent(knee_loc, knee_control)

        # Snappable Knee
        thigh_loc = pm.spaceLocator(n=side+"Thigh_to_kneeDist_LOC")
        foot_loc = pm.spaceLocator(n=side+"Knee_to_footDist_LOC")

        pm.matchTransform(thigh_loc, ik_chain["thigh"], pos=1)
        pm.matchTransform(foot_loc, ik_chain["foot"], pos=1)
        pm.parent(foot_loc, foot_control)

        thigh_to_knee_length = pm.distanceDimension(
            sp=thigh_loc.worldPosition.get(),
            ep=knee_loc.worldPosition.get()).getParent()
        thigh_to_knee_length.rename(side+"Thigh_to_kneeDistance")

        knee_to_foot_length = pm.distanceDimension(
            sp=knee_loc.worldPosition.get(),
            ep=foot_loc.worldPosition.get()).getParent()
        knee_to_foot_length.rename(side+"Knee_to_footDistance")

        shin_sdk = ik_chain["shin"].tx.inputs()[0]
        foot_sdk = ik_chain["foot"].tx.inputs()[0]

        stretch_blend = \
            pm.createNode("blendColors", n=side+"Knee_pv_stretchChoice")

        thigh_to_knee_length.distance >> stretch_blend.color1R
        shin_sdk.output >> stretch_blend.color2R
        stretch_blend.outputR >> ik_chain["shin"].tx

        knee_to_foot_length.distance >> stretch_blend.color1G
        foot_sdk.output >> stretch_blend.color2G
        stretch_blend.outputG >> ik_chain["foot"].tx

        pm.addAttr(knee_control,
                   ln="kneeSnap", at="float", k=1, min=0, max=1)
        knee_control.kneeSnap >> stretch_blend.blender
        return

    def _dual_knee_switch(self, no_flip_chain, pv_chain):
        ik_chain = self.ik_chain
        leg_settings = self.controls["leg_settings"]
        names = ["thigh", "shin", "foot"]
        side = self.side

        pm.addAttr(leg_settings,
                   longName="autoManualKneeBlend",
                   niceName="Auto/Manual Knee Blend",
                   attributeType="float",
                   keyable=1,
                   minValue=0,
                   maxValue=1,
                   defaultValue=1)

        nodes = []
        for n in names:
            pair_blend = pm.createNode(
                "pairBlend",
                n="{}{}_noFlipPVChoice".format(side, n.capitalize()))
            no_flip_chain[n].rotate >> pair_blend.inRotate1
            pv_chain[n].rotate >> pair_blend.inRotate2
            pair_blend.outRotate >> ik_chain[n].rotate

            no_flip_chain[n].translate >> pair_blend.inTranslate1
            pv_chain[n].translate >> pair_blend.inTranslate2
            pair_blend.outTranslate >> ik_chain[n].translate

            leg_settings.autoManualKneeBlend >> pair_blend.weight
            nodes += [pair_blend]

        pm.setDrivenKeyframe(leg_settings.knee_visibility,
                             cd=leg_settings.autoManualKneeBlend, dv=0, v=0)
        pm.setDrivenKeyframe(leg_settings.knee_visibility,
                             cd=leg_settings.autoManualKneeBlend, dv=0.001, v=1,
                             itt="linear", ott="linear")
        pm.setDrivenKeyframe(leg_settings.knee_visibility,
                             cd=leg_settings.autoManualKneeBlend, dv=1, v=1)
        return nodes
    
    def cleanup(self):
        side = self.side
        thigh_pivot = self.result_chain["thigh"].getTranslation(ws=1)

        groups = {k: None for k in ["leg", "dontTouch", "result", "ik", "fk"]}

        for k in ["result", "ik", "fk"]:
            n = k.upper() if len(k) == 2 else k
            grp = pm.group(em=1, n="{}Leg_{}Const_GRP".format(side, n))
            grp.setPivots(thigh_pivot, ws=1)
            groups[k] = grp

        groups["dontTouch"] = pm.group(em=1, n="dontTouch_GRP")
        groups["leg"] = pm.group(n=side+"Leg_GRP")

        pm.parent(self.result_chain["thigh"],
                  groups["result"])
        pm.parent(pm.ls(side+"*IK*JNT", side+"*_LOC", assemblies=1),
                  groups["ik"])
        pm.parent(self.controls["thigh_fk"].getParent(),
                  groups["fk"])

        pm.parent(groups["fk"], groups["leg"])
        pm.parent(self.controls["foot_ik"].getParent(), groups["leg"])
        pm.parent(self.controls["knee_ik"].getParent(), groups["leg"])

        for search in ["length", "Distance", "JNT", "Const_GRP"]:
            pm.parent(pm.ls(side+"*"+search, assemblies=1),
                      groups["dontTouch"])
        return groups

    def space_switch(self, controls):
        # Spaces
        side = self.side
        thigh_pivot = self.result_chain["thigh"].getTranslation(ws=1)

        spaces = {}  # hip, body, root
        for c in controls:
            k = c.split("_", 1)[0]
            spaces[k] = pm.spaceLocator(n="{}Leg_{}Space_LOC".format(side, k))
            spaces[k].t.set(thigh_pivot)
            pm.parent(spaces[k], c)

        const_groups = {
            "result": side+"Leg_resultConst_GRP",
            "ik": side+"Leg_IKConst_GRP",
            "fk": side+"Leg_FKConst_GRP"
        }

        # FK Rotation Space
        leg_settings_con = pm.PyNode(side+"Leg_settings_CON")
        pm.addAttr(leg_settings_con, ln="FK_rotationSpace", at="enum",
                   k=1, en=":".join(spaces.keys()))

        # --- SDK for result constrain group
        self._fk_rotation_space(
            spaces,
            driver=leg_settings_con.FK_rotationSpace,
            driven=const_groups["result"])

        # --- SDK for FK constrain group
        self._fk_rotation_space(
            spaces,
            driver=leg_settings_con.FK_rotationSpace,
            driven=const_groups["fk"])

        # Hip Drives Leg - point constraint hip space locator to const groups
        connect_space = spaces[controls[0].split("_", 1)[0]]
        for grp in const_groups.values():
            pm.pointConstraint(connect_space, grp, mo=1)
        return spaces
    
    def _fk_rotation_space(self, spaces, driver=None, driven=None):
        side = self.side
        
        orient_constraint = \
            pm.orientConstraint(spaces.values(), driven, mo=1)
        rotation_space_values = spaces.keys()

        for dv in rotation_space_values:
            # key all weights to 0
            map(lambda x:
                pm.setDrivenKeyframe(
                    x,
                    cd=driver,
                    dv=rotation_space_values.index(dv),
                    v=0,
                    itt="auto",
                    ott="step"),
                orient_constraint.listAttr(st="*Space_*"))

            # key weight matching driven value to 1
            weight = orient_constraint.listAttr(
                st="{}Leg_{}Space_LOC*".format(side, dv))

            pm.setDrivenKeyframe(
                weight,
                currentDriver=driver,
                driverValue=rotation_space_values.index(dv),
                value=1,
                itt="auto",
                ott="step"
            )
        return orient_constraint
