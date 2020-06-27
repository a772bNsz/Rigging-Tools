import pymel.core as pm
from collections import OrderedDict


class Rig:
    def __init__(self, root, side="", root_control=""):
        self.side = side
        self.root_control = root_control

        self.result_chain, self.ik_chain, self.fk_chain = \
            self._joint_chains(root, side)

        self.controls = self._controls(
            side, self.result_chain, self.ik_chain, self.fk_chain)

        self.twist_nodes = {}
        self.stretch_and_bend_ik_nodes = {}
        self.snap_nodes = {}

    @staticmethod
    def _joint_chains(root, side):
        names = OrderedDict({"upper": "upperArm"})
        names["lower"] = "foreArm"
        names["hand"] = "hand"
        names["end"] = "hand_end"

        result_chain = [root] + root.getChildren(ad=1)[::-1]
        pm.joint(result_chain[0], e=1, oj="xyz", sao="ydown", ch=1, zso=1)
        result_chain[-1].jointOrient.set(0, 0, 0)

        ik_chain, fk_chain = [pm.duplicate(result_chain) for i in range(2)]

        result_dict, ik_dict, fk_dict = [OrderedDict() for i in range(3)]

        for (k, v), r, ik, fk \
                in zip(names.items(), result_chain, ik_chain, fk_chain):
            name = v if "" == side else side + v[0].upper() + v[1:]

            result_dict[k] = r.rename(name + "_result_JNT")
            ik_dict[k] = ik.rename(name + "_IK_JNT")
            fk_dict[k] = fk.rename(name + "_FK_JNT")
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

    @staticmethod
    def create_twist_chain(curve, number=5, name="#"):
        chain = []
        for i in range(number):
            percent = i / (number - 1.0)
            position = pm.pointOnCurve(curve, pr=percent, p=1, top=1)
            n = str(i + 1).join(name.split("#"))
            chain += [pm.joint(p=position, a=1, n=n)]
        chain[0].setParent(None)
        return chain

    @staticmethod
    def ik_spline(oj, sao, up_axis, up_vectors, curve, chain, name="",
                  start_bind=None, end_bind=None):
        root, end = chain[0], chain[-1]

        # orient chain
        pm.joint(root, e=1, oj=oj, sao=sao, ch=1, zso=1)
        end.jointOrient.set(0, 0, 0)

        # IK spline handle
        handle, effector = pm.ikHandle(n=name + "_HDL",
                                       sj=root,
                                       ee=end,
                                       sol="ikSplineSolver",
                                       c=curve,
                                       ccv=0)
        effector.rename(name + "_EFF")
        curve.inheritsTransform.set(0)

        # skin bind joints spline curve
        if not start_bind:
            start_bind = pm.duplicate(root, po=1)[0]
        if not end_bind:
            end_bind = pm.duplicate(end, un=0)[0]
            end_bind.setParent(None)

        pm.skinCluster(
            start_bind, end_bind, curve, tsb=1, mi=2, n=name + "_SCL")

        # advanced twist settings
        upv1, upv2 = up_vectors

        if not up_axis:
            axis_direction = {
                "down": "Positive",
                "up": "Negative"
            }

            # Positive Z / Negative Y
            enum = " ".join(axis_direction[sao[1:]], oj[-1]).title()

            # spline handle up axis enum list
            handle_up_axis_enums = pm.attributeQuery("dWorldUpAxis",
                                                     node=handle,
                                                     listEnum=1)[0].split(":")

            # Positive Z = 3 / Negative Y = 1
            up_axis = handle_up_axis_enums.index(enum)

        handle.dTwistControlEnable.set(1)
        handle.dWorldUpType.set(4)  # object rotation up (start/end)
        handle.dWorldUpAxis.set(up_axis)
        handle.dWorldUpVector.set(upv1)
        handle.dWorldUpVectorEnd.set(upv2)

        start_bind.worldMatrix[0] >> handle.dWorldUpMatrix
        end_bind.worldMatrix[0] >> handle.dWorldUpMatrixEnd

        # update class attributes
        twist_nodes = {
            "handle": handle,
            "start_bind": start_bind,
            "end_bind": end_bind,
            "curve": curve,
            "chain": chain
        }
        return twist_nodes

    @staticmethod
    def stretch_spline(curve, chain, driver_attr="sx", name=""):
        curve_info = pm.arclen(curve, ch=1).rename(name + "Info")

        normalize_div = pm.createNode("floatMath", n=name + "_normalize_DIV")
        normalize_div.operation.set(3)  # divide
        curve_info.arcLength >> normalize_div.floatA
        normalize_div.floatB.set(curve_info.arcLength.get())

        for jnt in chain:
            normalize_div.outFloat >> jnt.attr(driver_attr)
        return True

    def _twist_upperarm(self):
        side = self.side
        name = side + "UpperArm"

        # twist chain
        start_point = self.result_chain["upper"].getTranslation(space="world")
        end_point = self.result_chain["lower"].getTranslation(space="world")
        curve = pm.curve(d=1,
                         p=[start_point, end_point],
                         k=[0, 1],
                         n=name + "_CRV")
        params = {
            "curve": curve,
            "name": name + "_seg#_JNT"
        }
        chain = self.create_twist_chain(**params)

        # ik spline
        params = {
            "oj": "xyz",  # joint orientation
            "sao": "ydown",  # secondary axis orientation
            "up_axis": 3,  # +z
            "up_vectors": [[0, 0, 1]] * 2,
            "curve": curve,
            "chain": chain,
            "name": name,
        }
        twisted = self.ik_spline(**params)
        start_bind = twisted["start_bind"]
        end_bind = twisted["end_bind"]

        start_bind.rename(side + "Arm_start_bind_JNT")
        end_bind.rename(side + "Arm_mid_bind_JNT")

        self.twist_nodes["upper"] = twisted

        # stretch
        params = {
            "curve": curve,
            "chain": chain,
            "name": name
        }
        self.stretch_spline(**params)
        return True

    def _twist_lowerarm(self):
        side = self.side
        name = side + "ForeArm"

        # twist chain
        start_point = self.result_chain["lower"].getTranslation(space="world")
        end_point = self.result_chain["hand"].getTranslation(space="world")
        curve = pm.curve(d=1,
                         p=[start_point, end_point],
                         k=[0, 1],
                         n=name + "_CRV")
        params = {
            "curve": curve,
            "name": name + "_seg#_JNT"
        }
        chain = self.create_twist_chain(**params)

        # ik spline
        params = {
            "oj": "xyz",  # joint orientation
            "sao": "ydown",  # secondary axis orientation
            "up_axis": 3,  # +z
            "up_vectors": [[0, 0, 1]] * 2,
            "curve": curve,
            "chain": chain,
            "start_bind": self.twist_nodes["upper"]["end_bind"],
            "name": name,
        }
        twisted = self.ik_spline(**params)
        start_bind = twisted["start_bind"]
        end_bind = twisted["end_bind"]

        end_bind.rename(side + "Arm_end_bind_JNT")

        self.twist_nodes["lower"] = twisted

        # stretch
        params = {
            "curve": curve,
            "chain": chain,
            "name": name
        }
        self.stretch_spline(**params)
        return True

    def twist(self):
        side = self.side
        twist_group = pm.group(em=1, n=side + "Arm_twist_GRP")
        self.twist_nodes["twist_group"] = twist_group

        self._twist_upperarm()
        self._twist_lowerarm()

        start_bind = self.twist_nodes["upper"]["start_bind"]
        mid_bind = self.twist_nodes["upper"]["end_bind"]
        end_bind = self.twist_nodes["lower"]["end_bind"]

        pm.pointConstraint(self.result_chain["upper"], start_bind, mo=1)
        pm.parentConstraint(self.result_chain["lower"], mid_bind, mo=1)
        pm.parentConstraint(self.result_chain["hand"], end_bind, mo=1)

        pm.hide(start_bind, mid_bind, end_bind)
        for k in ["upper", "lower"]:
            pm.parent(self.twist_nodes[k]["curve"],
                      self.twist_nodes[k]["handle"],
                      twist_group)
        return True

    def ikfk_switch(self):
        arm_settings = self.controls["arm_settings"]
        result_chain, ik_chain, fk_chain = \
            self.result_chain, self.ik_chain, self.fk_chain

        names = OrderedDict({"upper": "upperArm"})
        names["lower"] = "foreArm"
        names["hand"] = "hand"
        names["end"] = "hand_end"

        pm.addAttr(arm_settings, ln="FK_IK_blend", nn="FK/IK Blend",
                   at="float", k=1, min=0, max=1)

        nodes = []
        side = self.side
        for k, v in names.items():
            name = v if "" == side else side + v[0].upper() + v[1:]
            name += "_IKFKChoice"
            pair_blend = pm.createNode("pairBlend", n=name)
            fk_chain[k].rotate >> pair_blend.inRotate1
            ik_chain[k].rotate >> pair_blend.inRotate2
            pair_blend.outRotate >> result_chain[k].rotate

            fk_chain[k].translate >> pair_blend.inTranslate1
            ik_chain[k].translate >> pair_blend.inTranslate2
            pair_blend.outTranslate >> result_chain[k].translate

            arm_settings.FK_IK_blend >> pair_blend.weight
            nodes += [pair_blend]

        pm.addAttr(arm_settings, ln="IK_visibility", at="bool", k=0, h=1)
        pm.addAttr(arm_settings, ln="FK_visibility", at="bool", k=0, h=1)

        arm_settings.FK_visibility >> self.controls["upper"].getParent().v
        arm_settings.IK_visibility >> self.controls["arm"].v

        pm.setDrivenKeyframe(arm_settings.FK_visibility,
                             cd=arm_settings.FK_IK_blend, dv=0.999, v=1,
                             itt="linear", ott="linear")
        pm.setDrivenKeyframe(arm_settings.FK_visibility,
                             cd=arm_settings.FK_IK_blend, dv=1, v=0,
                             itt="linear", ott="linear")

        pm.setDrivenKeyframe(arm_settings.IK_visibility,
                             cd=arm_settings.FK_IK_blend, dv=0, v=0,
                             itt="linear", ott="linear")
        pm.setDrivenKeyframe(arm_settings.IK_visibility,
                             cd=arm_settings.FK_IK_blend, dv=0.001, v=1,
                             itt="linear", ott="linear")
        return nodes

    @staticmethod
    def stretch_fk(driver, driven):
        pm.addAttr(driver, ln="length", at="float", k=1, min=0, dv=1)

        driven = driven.tx
        driver = driver.length

        pm.setDrivenKeyframe(driven, cd=driver)
        pm.setInfinity(driven, poi="linear")
        pm.setDrivenKeyframe(driven, cd=driver, dv=0, v=0)
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

        # SDK setup
        for k in keys[:-1]:
            driver = self.controls[k]
            driven = driver.getChildren(type="transform")[0]
            self.stretch_fk(driver, driven)
        return True

    def stretch_and_bend_ik(self, name, joints=[], preferred_angle=[]):
        # upperarm, forearm, hand
        # thigh, shin, foot
        start, mid, end = joints

        if preferred_angle:
            mid.r.set(preferred_angle)
            mid.setPreferredAngles()
            mid.r.set(0, 0, 0)

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

        self.stretch_and_bend_ik_nodes = {
            "handle": handle,
            "length": length,
            "length_start": length_start,
            "length_end": length_end
        }
        return True

    def snap(self, controls, locators, handle, joints, length, stretch_blend):
        # pole vector constraint on IK rp handle for the elbow or knee
        snap_control, control = controls["snap"], controls["main"]
        snap_loc = pm.spaceLocator(n=locators["snap"])

        pm.parent(snap_loc, snap_control, r=1)
        pm.poleVectorConstraint(snap_loc, handle)

        # get distance for thigh and shin or upper arm and fore arm
        start, mid, end = joints
        start_loc = pm.spaceLocator(n=locators["start"])
        end_loc = pm.spaceLocator(n=locators["end"])

        pm.matchTransform(start_loc, start, pos=1)
        pm.matchTransform(end_loc, end, pos=1)
        pm.parent(end_loc, control)

        first_length = pm.distanceDimension(
            sp=start_loc.worldPosition.get(),
            ep=snap_loc.worldPosition.get()).getParent()
        first_length.rename(length["first"])

        second_length = pm.distanceDimension(
            sp=snap_loc.worldPosition.get(),
            ep=end_loc.worldPosition.get()).getParent()
        second_length.rename(length["second"])

        # blend between the set driven keys stretching and bending IK chain
        # in stretch_and_bend_ik() and this snappable elbow/knee setup
        mid_sdk = mid.tx.inputs()[0]
        end_sdk = end.tx.inputs()[0]
        stretch_blend = pm.createNode("blendColors", n=stretch_blend)

        first_length.distance >> stretch_blend.color1R
        mid_sdk.output >> stretch_blend.color2R
        stretch_blend.outputR >> mid.tx

        second_length.distance >> stretch_blend.color1G
        end_sdk.output >> stretch_blend.color2G
        stretch_blend.outputG >> end.tx

        attr = controls["attr"]
        pm.addAttr(snap_control, ln=attr, at="float", k=1, min=0, max=1)
        snap_control.attr(attr) >> stretch_blend.blender

        self.snap_nodes = {
            "locators": {
                "snap": snap_loc,
                "start": start_loc,
                "end": end_loc
            },
            "length": {
                "first": first_length,
                "second": second_length,
            },
            "stretch_blend": stretch_blend
        }
        return self.snap_nodes

    def ik(self):
        side = self.side

        # stretch and bend IK
        params = {
            "name": side + "Arm",
            "joints": [v for v in self.ik_chain.values()[:-1]],
            "preferred_angle": [0, 10, 0]
        }
        self.stretch_and_bend_ik(**params)

        handle = self.stretch_and_bend_ik_nodes["handle"]
        length_end = self.stretch_and_bend_ik_nodes["length_end"]
        arm_control = self.controls["arm"]
        pm.parent(handle, length_end, arm_control)

        stretch_and_bend_ik_nodes = self.stretch_and_bend_ik_nodes.values()
        pm.hide(stretch_and_bend_ik_nodes)

        # SC solver for hand IK
        hand = self.ik_chain["hand"]
        end = self.ik_chain["end"]
        handle, effector = pm.ikHandle(sj=hand,
                                       ee=end,
                                       sol="ikSCsolver",
                                       n=side + "Hand_HDL")
        effector.rename(side + "Hand_EFF")
        pm.parent(handle, arm_control)

        # snappable elbow
        params = {
            "controls": {
                "snap": self.controls["elbow"],
                "main": self.controls["arm"],
                "attr": "elbowSnap"
            },
            "locators": {
                "snap": side + "Elbow_LOC",
                "start": side + "UpperArm_to_elbowDistStart_LOC",
                "end": side + "Elbow_to_handDistEnd_LOC"
            },
            "joints": [v for v in self.ik_chain.values()[:-1]],
            "length": {
                "first": side + "UpperArm_to_elbow_distance",
                "second": side + "Elbow_to_hand_distance"
            },
            "handle": handle,
            "stretch_blend": side + "Elbow_stretchChoice"
        }
        self.snap(**params)

        for k in ["locators", "length"]:
            pm.hide(self.snap_nodes[k].values())
        return True
