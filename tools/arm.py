import pymel.core as pm
from collections import OrderedDict


class Twist:
    def __init__(self):
        self.name = None

        # create_chain()
        self.chain = None
        self.spline_curve = None

        # ik_spline()
        self.start_bind = None
        self.end_bind = None
        self.ik_handle = None

    def rename_chain(self, name="#"):
        num = len(self.chain)
        for i in range(num):
            self.chain[i].rename(str(i+1).join(name.split("#")))
        return self.chain

    def create_chain(self, start, end, number=5, name="#"):
        chain = []
        curve = pm.curve(d=1, p=[start, end], k=[0, 1])
        pm.select(cl=1)
        for i in range(number):
            percent = i / (number - 1.0)
            position = pm.pointOnCurve(curve, pr=percent, p=1, top=1)
            chain += [pm.joint(p=position, a=1)]

        self.chain = chain
        self.rename_chain(name=name)
        self.spline_curve = curve.rename(self.name + "_CRV")
        return True

    def ik_spline(self, oj="xyz", sao="ydown", upaxis=3, upv1=[0, 0, 1],
                  upv2=[0, 0, 1]):
        name = self.name
        root_joint = self.chain[0]
        end_joint = self.chain[-1]

        # orient joint chain
        pm.joint(root_joint, e=1, oj=oj, sao=sao, ch=1, zso=1)
        end_joint.jointOrient.set(0, 0, 0)

        # create ik spline handle
        handle, effector, curve = None, None, self.spline_curve
        if curve:
            handle, effector = pm.ikHandle(n=name + "_HDL",
                                           sj=root_joint,
                                           ee=end_joint,
                                           sol="ikSplineSolver",
                                           c=curve,
                                           ccv=0)
        else:
            handle, effector, curve = pm.ikHandle(n=name + "_HDL",
                                                  sj=root_joint,
                                                  ee=end_joint,
                                                  sol="ikSplineSolver")
            curve.rename(name + "_CRV")
        effector.rename(name + "_EFF")
        curve.inheritsTransform.set(0)

        # skin bind joints to spline curve
        start_bind, end_bind = self.start_bind, self.end_bind
        if not start_bind:
            start_bind = self.start_bind = pm.duplicate(root_joint, po=1)[0]
        if not end_bind:
            end_bind = self.end_bind = pm.duplicate(end_joint, un=0)[0]
            pm.parent(end_bind, w=1)

        pm.skinCluster(
            start_bind, end_bind, curve, tsb=1, mi=2, n=name + "_SCL")

        # ik spline handle advanced twist settings
        handle.dTwistControlEnable.set(1)
        handle.dWorldUpType.set(4)  # object rotation up (start/end)
        handle.dWorldUpAxis.set(upaxis)  # 3 = +z; 1 = -y
        handle.dWorldUpVector.set(upv1)
        handle.dWorldUpVectorEnd.set(upv2)

        start_bind.worldMatrix[0] >> handle.dWorldUpMatrix
        end_bind.worldMatrix[0] >> handle.dWorldUpMatrixEnd

        # update attributes
        self.ik_handle = handle
        self.spline_curve = curve
        self.start_bind = start_bind
        self.end_bind = end_bind
        return


class Stretch:
    def __init__(self):
        # ik() snap() inputs
        self.chain = []

        # ik() outputs
        self.ik_handle = None
        self.length_start = None
        self.length_end = None

        # snap() inputs
        self.snap_dict = {}

    @staticmethod
    def fk(driver, driven, driver_attr="length", driven_attr="tx"):
        pm.addAttr(driver, ln=driver_attr, at="float", k=1, min=0, dv=1)

        driver = driver.attr(driver_attr)  # driver.length
        driven = driven.attr(driven_attr)  # driven.tx

        pm.setDrivenKeyframe(driven, cd=driver)
        pm.setInfinity(driven, poi="linear")
        pm.setDrivenKeyframe(driven, cd=driver, dv=0, v=0)
        return True

    def spline_curve(self, curve, driver_attr="sx", name=""):
        chain = self.chain

        curve_info = pm.arclen(curve, ch=1).rename(name + "Info")

        normalize_div = pm.createNode("floatMath", n=name + "_normalize_DIV")
        normalize_div.operation.set(3)  # divide
        curve_info.arcLength >> normalize_div.floatA
        normalize_div.floatB.set(curve_info.arcLength.get())

        for jnt in chain:
            normalize_div.outFloat >> jnt.attr(driver_attr)
        return

    def ik(self, name=""):
        # upperarm, forearm, hand
        # thigh, shin, foot
        start, mid, end = self.chain

        # RP solver
        handle, effector = pm.ikHandle(sj=start, ee=end, sol="ikRPsolver")
        handle.rename(name + "HDL")
        effector.rename(name + "EFF")

        # IK stretches and bends at default length
        length_start = pm.spaceLocator(n=name + "_IK_lengthStart_LOC")
        length_end = pm.spaceLocator(n=name + "_IK_lengthEnd_LOC")

        pm.matchTransform(length_start, start, pos=1)
        pm.matchTransform(length_end, end, pos=1)

        length = pm.distanceDimension(
            sp=length_start.worldPosition.get(),
            ep=length_end.worldPosition.get()).getParent()
        length.rename(name + "_IK_length")

        limb1_length = mid.tx.get()
        limb2_length = end.tx.get()
        sum_length = limb1_length + limb2_length

        # --- SDK for first limb
        pm.setDrivenKeyframe(
            mid.tx, cd=length.distance, dv=sum_length, v=limb1_length)
        pm.setDrivenKeyframe(
            mid.tx, cd=length.distance, dv=sum_length * 2, v=limb1_length * 2)
        pm.setInfinity(mid.tx, poi="linear")

        # --- SDK for second limb
        pm.setDrivenKeyframe(
            end.tx, cd=length.distance, dv=sum_length, v=limb2_length)
        pm.setDrivenKeyframe(
            end.tx, cd=length.distance, dv=sum_length * 2, v=limb2_length * 2)
        pm.setInfinity(end.tx, poi="linear")

        # cleanup
        pm.hide(handle, length_start, length_end, length)

        self.ik_handle = handle
        self.length_start = length_start
        self.length_end = length_end
        return True

    def snap(self):
        snap_dict = self.snap_dict
        handle = self.ik_handle  # arm / leg
        snap_loc = pm.spaceLocator(n=snap_dict["snap_loc"])  # elbow / knee

        snap_control = snap_dict["snap_control"]
        pm.parent(snap_loc, snap_control, r=1)
        pm.poleVectorConstraint(snap_loc, handle)

        # upperarm, forearm, hand
        # thigh, shin, foot
        start, mid, end = self.chain

        start_loc = pm.spaceLocator(n=snap_dict["start_loc"])
        end_loc = pm.spaceLocator(n=snap_dict["end_loc"])

        control = snap_dict["control"]
        pm.matchTransform(start_loc, start, pos=1)
        pm.matchTransform(end_loc, end, pos=1)
        pm.parent(end_loc, control)

        first_length = pm.distanceDimension(
            sp=start_loc.worldPosition.get(),
            ep=snap_loc.worldPosition.get()).getParent()
        first_length.rename(snap_dict["first_length"])

        second_length = pm.distanceDimension(
            sp=snap_loc.worldPosition.get(),
            ep=end_loc.worldPosition.get()).getParent()
        second_length.rename(snap_dict["second_length"])

        mid_sdk = mid.tx.inputs()[0]
        end_sdk = end.tx.inputs()[0]

        stretch_blend = \
            pm.createNode("blendColors", n=snap_dict["stretch_blend"])

        first_length.distance >> stretch_blend.color1R
        mid_sdk.output >> stretch_blend.color2R
        stretch_blend.outputR >> mid.tx

        second_length.distance >> stretch_blend.color1G
        end_sdk.output >> stretch_blend.color2G
        stretch_blend.outputG >> end.tx

        pm.addAttr(snap_control,
                   ln=snap_dict["attr"], at="float", k=1, min=0, max=1)
        snap_control.attr(snap_dict["attr"]) >> stretch_blend.blender

        self.snap_dict = {
            "snap_loc": snap_loc,
            "start_loc": start_loc,
            "end_loc": end_loc,
            "first_length": first_length,
            "second_length": second_length,
            "stretch_blend": stretch_blend
        }
        return True


class Rig:
    def __init__(self, root, side="", root_control=""):
        self.side = side
        self.root_control = root_control

        self.result_chain, self.ik_chain, self.fk_chain = \
            self._joint_chains(root, side)

        self.controls = self._controls(
            side, self.result_chain, self.ik_chain, self.fk_chain)

    @staticmethod
    def _joint_chains(root, side):
        result_dict = OrderedDict({"upper": "upperArm_result_JNT"})
        result_dict["lower"] = "foreArm_result_JNT"
        result_dict["hand"] = "hand_result_JNT"
        result_dict["end"] = "hand_end_result_JNT"

        result_chain = [root] + root.getChildren(ad=1)[::-1]

        for (k, v), jnt in zip(result_dict.items(), result_chain):
            name = v if "" == side else side + v[0].upper() + v[1:]
            result_dict[k] = jnt.rename(name)

        pm.joint(result_chain[0], e=1, oj="xyz", sao="ydown", ch=1, zso=1)
        result_chain[-1].jointOrient.set(0, 0, 0)

        ik_chain = pm.duplicate(result_chain)
        fk_chain = pm.duplicate(result_chain)
        for ik, fk in zip(ik_chain, fk_chain):
            name = ik.replace("result", "IK")
            ik.rename(name)
            name = fk.replace("result", "FK")
            fk.rename(name)
        ik_chain[0].rename(ik_chain[0][:-1])
        fk_chain[0].rename(fk_chain[0][:-1])

        ik_dict = OrderedDict()
        fk_dict = OrderedDict()
        for k, ik, fk in zip(result_dict.keys(), ik_chain, fk_chain):
            ik_dict[k] = ik
            fk_dict[k] = fk
        return result_dict, ik_dict, fk_dict

    @staticmethod
    def _controls(side, result_chain, ik_chain, fk_chain):
        arm_settings = pm.spaceLocator(n=side + "Arm_settings_CON")
        pm.matchTransform(arm_settings, result_chain["hand"], pos=1)
        pm.parentConstraint(result_chain["hand"], arm_settings, mo=1)
        controls = OrderedDict({"arm_settings": arm_settings})

        # leftUpperArm_FK_CON
        upper_fk = pm.spaceLocator(n=fk_chain["upper"].replace("JNT", "CON"))
        pm.matchTransform(upper_fk, fk_chain["upper"])
        controls["upper"] = upper_fk

        # leftForeArm_FK_CON
        lower_fk = pm.spaceLocator(n=fk_chain["lower"].replace("JNT", "CON"))
        lower_fk.rotateOrder.set(3)  # xzy
        pm.matchTransform(lower_fk, fk_chain["lower"])
        controls["lower"] = lower_fk

        # leftHand_FK_CON
        hand_fk = pm.spaceLocator(n=fk_chain["hand"].replace("JNT", "CON"))
        hand_fk.rotateOrder.set(5)  # zyx
        pm.matchTransform(hand_fk, fk_chain["hand"])
        controls["hand"] = hand_fk

        # leftElbow_CON
        name = "elbow_CON" if "" == side else side + "Elbow_CON"
        elbow_ik = pm.spaceLocator(n=name)
        pm.matchTransform(elbow_ik, ik_chain["lower"], pos=1)
        pm.move(elbow_ik, -10, r=1, z=1)
        controls["elbow"] = elbow_ik

        # leftArm_CON
        name = "arm_CON" if "" == side else side + "Arm_CON"
        arm_ik = pm.spaceLocator(n=name)
        arm_ik.rotateOrder.set(5)  # zyx
        pm.matchTransform(arm_ik, ik_chain["hand"], pos=1)
        controls["arm"] = arm_ik

        if pm.objExists("settings_GRP"):
            pm.parent(arm_settings, "settings_GRP")
        else:
            pm.group(n="settings_GRP", em=1)
            pm.parent(arm_settings, "settings_GRP")

        for con in controls.values()[1:-2]:
            grp = pm.duplicate(con, n=con.replace("CON", "OFS"))[0]
            pm.delete(grp.getShapes())
            pm.parent(con, grp)
        return controls

    def twist(self):
        side = self.side
        twist_group = pm.group(em=1, n=side + "Arm_twist_GRP")

        # upper arm
        start = self.result_chain["upper"].getTranslation(space="world")
        end = self.result_chain["lower"].getTranslation(space="world")

        upperarm = Twist()
        upperarm.name = side + "UpperArm"
        upperarm.create_chain(
            start, end, number=5, name=side + "UpperArm_seg#_JNT")

        upperarm.ik_spline()
        upperarm.start_bind.rename(side + "Arm_start_bind_JNT")
        upperarm.end_bind.rename(side + "Arm_mid_bind_JNT")

        pm.hide(upperarm.start_bind, upperarm.end_bind)

        pm.pointConstraint(
            self.result_chain["upper"], upperarm.start_bind, mo=1)
        pm.parentConstraint(
            self.result_chain["lower"], upperarm.end_bind, mo=1)

        pm.parent(upperarm.spline_curve, upperarm.ik_handle, twist_group)

        upperarm_stretch = Stretch()
        upperarm.chain = upperarm.chain[:-1]
        curve = upperarm.spline_curve
        name = upperarm.name
        upperarm_stretch.spline_curve(curve, name=name)

        # lower arm
        start = end
        end = self.result_chain["hand"].getTranslation(space="world")

        lowerarm = Twist()
        lowerarm.name = side + "ForeArm"
        lowerarm.create_chain(
            start, end, number=5, name=side + "ForeArm_seg#_JNT")

        lowerarm.start_bind = upperarm.end_bind
        lowerarm.ik_spline()
        lowerarm.end_bind.rename(side + "Arm_end_bind_JNT")

        pm.hide(lowerarm.start_bind, lowerarm.end_bind)

        pm.parentConstraint(
            self.result_chain["lower"], lowerarm.start_bind, mo=1)
        pm.parentConstraint(
            self.result_chain["hand"], lowerarm.end_bind, mo=1)

        lowerarm_stretch = Stretch()
        lowerarm.chain = lowerarm.chain[:-1]
        curve = lowerarm.spline_curve
        name = lowerarm.name
        lowerarm_stretch.spline_curve(curve, name=name)

        pm.parent(lowerarm.spline_curve, lowerarm.ik_handle, twist_group)
        twist_group.hide()
        return True

    def fk(self):
        # parent controls to their hierarchy
        keys = ["upper", "lower", "hand"]
        parent = None
        for k in keys:
            offset = self.controls[k].getParent()
            pm.parent(offset, parent)
            parent = self.controls[k]

        # parent constrain controls to their joint
        parent = None
        for k in keys:
            pm.parentConstraint(self.controls[k], self.fk_chain[k])
            parent = self.controls[k]

        # upper arm
        stretch = Stretch()
        driver = self.controls["upper"]
        driven = self.controls["lower"].getParent()
        stretch.fk(driver, driven)

        # fore arm
        stretch = Stretch()
        driver = self.controls["lower"]
        driven = self.controls["hand"].getParent()
        stretch.fk(driver, driven)
        return True

    def ik(self):
        arm = Stretch()

        # STRETCH AND BEND IK
        lowerarm = self.ik_chain["lower"]
        lowerarm.ry.set(10)
        lowerarm.setPreferredAngles()
        lowerarm.ry.set(0)

        arm.chain = [v for v in self.ik_chain.values()[:-1]]  # no hand_end
        arm.ik(name=self.side + "Arm")
        pm.parent(arm.ik_handle, arm.length_end, self.controls["arm"])

        # SC solver for hand IK
        hand = self.ik_chain["hand"]
        end = self.ik_chain["end"]
        handle, effector = pm.ikHandle(sj=hand, ee=end, sol="ikSCsolver")
        handle.rename(self.side + "Hand_HDL")
        effector.rename(self.side + "Hand_EFF")
        pm.parent(handle, self.controls["arm"])

        # SNAPPABLE ELBOW
        side = self.side
        arm.snap_dict = {
            "snap_control": self.controls["elbow"],
            "attr": "elbowSnap",
            "control": self.controls["arm"],
            "snap_loc": side + "Elbow_LOC",
            "start_loc": side + "UpperArm_to_elbowDistStart_LOC",
            "end_loc": side + "Elbow_to_handDistEnd_LOC",
            "first_length": side + "UpperArm_to_elbow_distance",
            "second_length": side + "Elbow_to_hand_distance",
            "stretch_blend": side + "Elbow_stretchChoice"
        }
        arm.snap()

        # HYBRID ELBOW
        self.hybrid_elbow()
        return True

    def hybrid_elbow(self):
        elbow_control = self.controls["elbow"]

        # HYBRID CONTROLS
        hybrid_controls = OrderedDict()
        parent = None
        for k in ["lower", "hand"]:
            v = self.ik_chain[k]

            name = v.replace(self.side, self.side + "Elbow")
            name = name.replace("JNT", "CON")
            name = name.replace("IK", "FK")
            con = pm.spaceLocator(n=name)
            pm.matchTransform(con, v)

            ofs, = pm.duplicate(con, n=name.replace("CON", "OFS"))
            pm.delete(ofs.getShapes())
            pm.parent(con, ofs)

            pm.parent(ofs, parent)
            parent = con

            hybrid_controls[k] = con

        pm.matchTransform(hybrid_controls["lower"].getParent(),
                          elbow_control,
                          pos=1)
        pm.parent(hybrid_controls["lower"].getParent(), elbow_control)

        # FK STRETCH ON HYBRID CONTROLS
        stretch = Stretch()
        driver = hybrid_controls["lower"]
        driven = hybrid_controls["hand"].getParent()
        stretch.fk(driver, driven)

        # SWITCH BETWEEN IK ARM CONTROL AND FK HYBRID CONTROLS
        elbow_control.elbowSnap.set(1)

        ik_control = self.controls["arm"]
        fk_control = hybrid_controls["hand"]

        ik_const_grp = pm.group(em=1, n=self.side + "Arm_IKConst_GRP")
        pm.matchTransform(ik_const_grp, ik_control, pos=1)
        pm.matchTransform(ik_const_grp, fk_control, rot=1)

        children = ik_control.getChildren(ad=1, type="transform")
        pm.parent(children, ik_const_grp)

        parent_constraint = pm.parentConstraint(ik_control, ik_const_grp, mo=1)
        pm.parentConstraint(fk_control, ik_const_grp)

        # SWITCH ATTRIBUTES
        pm.addAttr(elbow_control,
                   ln="FK_forearmBlend", k=1, at="float", min=0, max=1)
        fk_control_root = hybrid_controls["lower"].getParent()

        # --- IK arm control enabled
        attr = parent_constraint.listAttr(st=ik_control + "W*")[0]
        pm.setDrivenKeyframe(
            attr,
            cd=elbow_control.FK_forearmBlend,
            dv=0,
            v=1,
            itt="linear",
            ott="linear"
        )
        attr = parent_constraint.listAttr(st=fk_control + "W*")[0]
        pm.setDrivenKeyframe(
            attr,
            cd=elbow_control.FK_forearmBlend,
            dv=0,
            v=0,
            itt="linear",
            ott="linear"
        )
        pm.setDrivenKeyframe(
            ik_control.v,
            cd=elbow_control.FK_forearmBlend,
            dv=0,
            v=1,
            itt="linear",
            ott="linear"
        )
        pm.setDrivenKeyframe(
            fk_control_root.v,
            cd=elbow_control.FK_forearmBlend,
            dv=0,
            v=0,
            itt="linear",
            ott="linear"
        )

        # --- FK hybrid controls enabled
        attr = parent_constraint.listAttr(st=ik_control + "W*")[0]
        pm.setDrivenKeyframe(
            attr,
            cd=elbow_control.FK_forearmBlend,
            dv=1,
            v=0,
            itt="linear",
            ott="linear"
        )
        attr = parent_constraint.listAttr(st=fk_control + "W*")[0]
        pm.setDrivenKeyframe(
            attr,
            cd=elbow_control.FK_forearmBlend,
            dv=1,
            v=1,
            itt="linear",
            ott="linear"
        )
        pm.setDrivenKeyframe(
            ik_control.v,
            cd=elbow_control.FK_forearmBlend,
            dv=1,
            v=0,
            itt="linear",
            ott="linear"
        )
        pm.setDrivenKeyframe(
            fk_control_root.v,
            cd=elbow_control.FK_forearmBlend,
            dv=0.001,
            v=1,
            itt="linear",
            ott="linear"
        )
        return True
