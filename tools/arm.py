import pymel.core as pm
from collections import OrderedDict


class Rig:
    def __init__(self, root, side="", root_control=""):
        self.side = side
        self.root_control = root_control

        self.result_chain, self.ik_chain, self.fk_chain = \
            self._joint_chains(root, side)

        self.groups = self._groups(side)
        self.controls = self._controls(
            side, self.result_chain, self.ik_chain, self.fk_chain)

        self.twist_nodes = {}
        self.stretch_and_bend_ik_nodes = {}
        self.snap_nodes = {}
        self.hybrid_elbow_nodes = {}

    @staticmethod
    def _joint_chains(root, side):
        names = OrderedDict({"upper": "upperArm"})
        names["lower"] = "foreArm"
        names["hand"] = "hand"
        names["end"] = "hand_end"

        result_chain = [root] + root.getChildren(ad=1)[::-1]
        if "right" != side:
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

    def _groups(self, side):
        groups = OrderedDict(
            {"arm": pm.group(em=1, n=side + "Arm_GRP")})
        pm.parent(groups["arm"], self.root_control)

        groups["dont_touch"] = pm.group(em=1, n="dontTouch_GRP")
        pm.parent(groups["dont_touch"], groups["arm"])

        root_pivot = self.result_chain["upper"].getTranslation(ws=1)

        # example: leftArm_IKConst_GRP
        name = "arm" if "" == side else side + "Arm"

        for k in ["result", "IK", "FK"]:
            grp = pm.group(em=1, n=name + "_{}Const_GRP".format(k))

            if k == "FK":
                grp.setParent(groups["arm"])
            else:
                grp.setParent(groups["dont_touch"])
            grp.setPivots(root_pivot)

            groups[k.lower()] = grp  # groups["ik"]

        grp = pm.group(em=1, n=name + "Base_IKConst_GRP")
        grp.setParent(groups["dont_touch"])
        grp.setPivots(root_pivot)
        groups["base_ik"] = grp

        items = [groups["arm"], groups["dont_touch"]]
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, lock=0, keyable=0, cb=1)
        return groups

    @staticmethod
    def _controls(side, result_chain, ik_chain, fk_chain):
        arm_settings = pm.spaceLocator(n=side + "Arm_settings_CON")
        pm.matchTransform(arm_settings, result_chain["hand"], pos=1)
        pm.parentConstraint(result_chain["hand"], arm_settings, mo=1)
        pm.scaleConstraint(result_chain["hand"], arm_settings)
        controls = OrderedDict({"arm_settings": arm_settings})

        # leftArm_gimbal_corr_CON
        name = "arm_gimbal_corr_CON" if "" == side \
            else side + "Arm_gimbal_corr_CON"
        gimbal_ik = pm.spaceLocator(n=name)
        pm.matchTransform(gimbal_ik, fk_chain["upper"])
        controls["gimbal"] = gimbal_ik

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
            grp = pm.group(n="settings_GRP", em=1)
            pm.parent(arm_settings, grp)

            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(grp.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(grp.v, lock=0, keyable=0, cb=1)

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
    def stretch_spline(curve, chain, control, name="", squash=0):
        curve_info = pm.arclen(curve, ch=1).rename(name + "Info")

        n = "globalScale_" + name + "Normalize_DIV"
        global_scale = pm.createNode("floatMath", n=n)
        global_scale.operation.set(3)  # divide

        curve_info.arcLength >> global_scale.floatA
        control >> global_scale.floatB

        n = name + "_stretchPercent_DIV"
        stretch_percent = pm.createNode("floatMath", n=n)
        stretch_percent.operation.set(3)  # divide

        global_scale.outFloat >> stretch_percent.floatA
        stretch_percent.floatB.set(curve_info.arcLength.get())

        for jnt in chain:
            stretch_percent.outFloat >> jnt.sx

        if squash:
            n = name + "_sqrtStretch_POW"
            sqrt_stretch = pm.createNode("floatMath", n=n)
            sqrt_stretch.operation.set(6)  # power

            stretch_percent.outFloat >> sqrt_stretch.floatA
            sqrt_stretch.floatB.set(0.5)

            n = name + "_stretchInvert_DIV"
            stretch_invert = pm.createNode("floatMath", n=n)
            stretch_invert.operation.set(3)

            stretch_invert.floatA.set(1)
            sqrt_stretch.outFloat >> stretch_invert.floatB

            for jnt in chain:
                stretch_invert.outFloat >> jnt.sy
                stretch_invert.outFloat >> jnt.sz
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
            "control": self.root_control.sx,
            "name": name,
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
        end_bind = twisted["end_bind"]

        end_bind.rename(side + "Arm_end_bind_JNT")

        self.twist_nodes["lower"] = twisted

        # stretch
        params = {
            "curve": curve,
            "chain": chain,
            "control": self.root_control.sx,
            "name": name,
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

        pm.parent(self.twist_nodes["upper"]["chain"][0],
                  self.twist_nodes["lower"]["chain"][0],
                  start_bind, mid_bind, end_bind,
                  twist_group)

        pm.parent(twist_group, self.groups["dont_touch"])

        for at in "trs":
            for ax in "xyz":
                pm.setAttr(twist_group.attr(at + ax), lock=1, keyable=0)
        pm.setAttr(twist_group.v, lock=0, keyable=0, cb=1)
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

        arm_settings.FK_visibility >> self.controls["gimbal"].getParent().v
        arm_settings.IK_visibility >> self.controls["arm"].v
        arm_settings.IK_visibility >> self.controls["elbow"].v

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

        pm.parent(self.result_chain["upper"], self.groups["result"])

        self.groups["arm"].v >> arm_settings.v

        for at in "trs":
            for ax in "xyz":
                pm.setAttr(arm_settings.attr(at + ax), lock=1, keyable=0)
        pm.setAttr(arm_settings.v, lock=1, keyable=0)
        return nodes

    @staticmethod
    def stretch_fk(driver, driven):
        pm.addAttr(driver, ln="length", at="float", k=1, min=0, dv=1)

        driven = driven.tx
        driver = driver.length

        pm.setDrivenKeyframe(driven, cd=driver,
                             itt="spline", ott="spline")
        pm.setInfinity(driven, poi="linear")
        pm.setDrivenKeyframe(driven, cd=driver,
                             dv=0, v=0, itt="spline", ott="spline")
        return True

    def fk(self):
        # parent controls to their hierarchy
        keys = ["gimbal", "upper", "lower", "hand"]
        parent = None
        for k in keys:
            offset = self.controls[k].getParent()
            pm.parent(offset, parent)
            parent = self.controls[k]

        gimbal_ofs = self.controls["gimbal"].getParent()
        gimbal_ofs.setParent(self.groups["fk"])

        # parent constrain controls to their joint
        parent = None
        for k in keys[1:]:
            pm.parentConstraint(self.controls[k], self.fk_chain[k])
            parent = self.controls[k]

        # SDK setup
        for k in keys[1:-1]:
            driver = self.controls[k]
            driven = driver.getChildren(type="transform")[0]
            self.stretch_fk(driver, driven)

        # clean up
        pm.parent(self.fk_chain["upper"], self.groups["dont_touch"])
        self.fk_chain["upper"].v.set(0)

        control_offsets = []
        controls = []
        for con in self.controls.values()[1:5]:
            control_offsets += [con.getParent()]
            controls += [con]

        items = control_offsets + [self.groups["fk"]]
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, lock=1, keyable=0)
        pm.setAttr(self.groups["fk"].v, lock=0, cb=1)

        for i in controls:
            for at in "ts":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, lock=1, keyable=0)
        return True

    def stretch_and_bend_ik(self, name, handle, joints=[]):
        # upperarm, forearm, hand
        # thigh, shin, foot
        start, mid, end = joints

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
            mid.tx, cd=length.distance, dv=sum_length, v=limb1_length,
            itt="spline", ott="spline")
        pm.setDrivenKeyframe(
            mid.tx, cd=length.distance, dv=sum_length * 2, v=limb1_length * 2,
            itt="spline", ott="spline")
        pm.setInfinity(mid.tx, poi="linear")

        # --- SDK for second limb
        pm.setDrivenKeyframe(
            end.tx, cd=length.distance, dv=sum_length, v=limb2_length,
            itt="spline", ott="spline")
        pm.setDrivenKeyframe(
            end.tx, cd=length.distance, dv=sum_length * 2, v=limb2_length * 2,
            itt="spline", ott="spline")
        pm.setInfinity(end.tx, poi="linear")

        # global scale
        params = {
            "control": self.root_control.sx,
            "length": length.distance,
            "name": "globalScale_" + name + "Normalize_DIV"
        }
        scale_node = self.scalable(**params)

        # cleanup
        pm.hide(handle, length_start, length_end, length)

        self.stretch_and_bend_ik_nodes = {
            "handle": handle,
            "length": length,
            "length_start": length_start,
            "length_end": length_end,
            "scale": scale_node
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
        stretch_blend.color2B.set(0)

        first_length.distance >> stretch_blend.color1R
        mid_sdk.output >> stretch_blend.color2R
        stretch_blend.outputR >> mid.tx

        second_length.distance >> stretch_blend.color1G
        end_sdk.output >> stretch_blend.color2G
        stretch_blend.outputG >> end.tx

        attr = controls["attr"]
        pm.addAttr(snap_control, ln=attr, at="float", k=1, min=0, max=1)
        snap_control.attr(attr) >> stretch_blend.blender

        # global scale
        params = {
            "control": self.root_control.sx,
            "length": None,
            "name": None
        }

        scale_nodes = []
        for length in [first_length, second_length]:
            params["length"] = length.distance

            # globalScale_leftUpperArm_to_elbowNormalize_DIV
            name = "globalScale_" + length.rsplit("_", 1)[0] + "Normalize_DIV"
            params["name"] = name
            scale_nodes += [self.scalable(**params)]

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
            "scale": {
                "first": scale_nodes[0],
                "second": scale_nodes[1]
            },
            "stretch_blend": stretch_blend
        }
        return self.snap_nodes

    def hybrid_elbow(self, ik_const_grp):
        side = self.side

        # controls and their offsets
        hybrid_controls = OrderedDict()
        parent = None
        for k in ["lower", "hand"]:
            v = self.fk_chain[k]

            name = v.replace(side, side + "Elbow")
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

        elbow_control = self.controls["elbow"]
        fk_control_root = hybrid_controls["lower"].getParent()

        pm.parent(fk_control_root, elbow_control)
        fk_control_root.t.set(0, 0, 0)

        # FK stretch on forearm control
        driver = hybrid_controls["lower"]
        driven = hybrid_controls["hand"].getParent()
        self.stretch_fk(driver, driven)

        # blend between IK/FK with parent constraint and constrain group
        arm_control = self.controls["arm"]
        elbow_hand_control = hybrid_controls["hand"]

        pm.matchTransform(ik_const_grp, arm_control, pos=1)
        pm.matchTransform(ik_const_grp, elbow_hand_control, rot=1)

        children = arm_control.getChildren(ad=1, type="transform")
        pm.parent(children, ik_const_grp)

        parent_constraint = \
            pm.parentConstraint(arm_control, ik_const_grp, mo=1)
        pm.parentConstraint(elbow_hand_control, ik_const_grp)

        # update visibility connections on arm control
        pm.addAttr(elbow_control,
                   ln="forearm_FK_visibility", k=1, at="bool")
        hybrid_fk_visibility = hybrid_controls["lower"].getParent().v
        elbow_control.forearm_FK_visibility >> hybrid_fk_visibility
        
        ik_vis_grp = pm.group(em=1, n=side + "Arm_IK_vis_GRP")
        pm.matchTransform(ik_vis_grp, arm_control)
        pm.parent(arm_control, ik_vis_grp)

        settings_control = self.controls["arm_settings"]
        settings_control.IK_visibility >> ik_vis_grp.v
        settings_control.IK_visibility // arm_control.v

        # SDK for elbow control's FK Forearm Blend
        pm.addAttr(elbow_control,
                   ln="FK_forearmBlend", k=1, at="float", min=0, max=1)

        # --- FK Forearm Blend = 0
        # left arm control = 1
        # left elbow hand control = 0
        # .forearm_FK_visibility = 0
        attr = parent_constraint.listAttr(st=arm_control + "W*")[0]
        pm.setDrivenKeyframe(
            attr,
            cd=elbow_control.FK_forearmBlend,
            dv=0,
            v=1,
            itt="linear",
            ott="linear"
        )
        attr = parent_constraint.listAttr(st=elbow_hand_control + "W*")[0]
        pm.setDrivenKeyframe(
            attr,
            cd=elbow_control.FK_forearmBlend,
            dv=0,
            v=0,
            itt="linear",
            ott="linear"
        )
        pm.setDrivenKeyframe(
            elbow_control.forearm_FK_visibility,
            cd=elbow_control.FK_forearmBlend,
            dv=0,
            v=0,
            itt="linear",
            ott="linear"
        )

        # --- FK Forearm Blend = 0.001
        # .forearm_FK_visibility = 1
        pm.setDrivenKeyframe(
            elbow_control.forearm_FK_visibility,
            cd=elbow_control.FK_forearmBlend,
            dv=0.001,
            v=1,
            itt="linear",
            ott="linear"
        )

        # --- FK Forearm Blend = 0.999
        # left arm control visibility = 1
        pm.setDrivenKeyframe(
            arm_control.v,
            cd=elbow_control.FK_forearmBlend,
            dv=0.999,
            v=1,
            itt="linear",
            ott="linear"
        )

        # --- FK Forearm Blend = 1
        # left arm control = 0
        # left elbow hand control = 1
        # left arm control visibility = 0
        attr = parent_constraint.listAttr(st=arm_control + "W*")[0]
        pm.setDrivenKeyframe(
            attr,
            cd=elbow_control.FK_forearmBlend,
            dv=1,
            v=0,
            itt="linear",
            ott="linear"
        )
        attr = parent_constraint.listAttr(st=elbow_hand_control + "W*")[0]
        pm.setDrivenKeyframe(
            attr,
            cd=elbow_control.FK_forearmBlend,
            dv=1,
            v=1,
            itt="linear",
            ott="linear"
        )
        pm.setDrivenKeyframe(
            arm_control.v,
            cd=elbow_control.FK_forearmBlend,
            dv=1,
            v=0,
            itt="linear",
            ott="linear"
        )

        # cleanup
        elbow_control.v.setLocked(1)
        elbow_control.v.setKeyable(1)

        self.hybrid_elbow_nodes = {
            "ik_const": ik_const_grp,
            "ik_vis": ik_vis_grp
        }
        self.hybrid_elbow_nodes.update(hybrid_controls)
        return hybrid_controls

    @staticmethod
    def scalable(control, length, name):
        if isinstance(control, pm.Attribute) \
                and isinstance(length, pm.Attribute):
            pass
        else:
            print ">> need attribute for parameter"
            return

        global_scale = pm.createNode("floatMath", n=name)
        global_scale.operation.set(3)
        connections = length.outputs(p=1)

        length >> global_scale.floatA
        control >> global_scale.floatB
        for i in connections:
            global_scale.outFloat >> i
        return global_scale

    def ik(self):
        arm_group = self.groups["arm"]
        base_ik_const_group = self.groups["base_ik"]
        ik_const_group = self.groups["ik"]
        dont_group = self.groups["dont_touch"]

        self.ik_chain["upper"].setParent(base_ik_const_group)

        arm_control = self.controls["arm"]
        arm_control.setParent(arm_group)

        elbow_control = self.controls["elbow"]
        elbow_control.setParent(arm_group)

        side = self.side
        name = side + "Arm"

        # RP solver
        start, mid, end = [v for v in self.ik_chain.values()[:-1]]

        mid.r.set([0, 10, 0])
        mid.setPreferredAngles()
        mid.r.set(0, 0, 0)

        handle, effector = pm.ikHandle(sj=start, ee=end, sol="ikRPsolver")
        handle.rename(name + "HDL")
        effector.rename(name + "EFF")

        handle.setParent(ik_const_group)

        # stretch and bend IK
        params = {
            "name": name,
            "joints": [start, mid, end],
            "handle": handle
        }
        self.stretch_and_bend_ik(**params)

        handle = self.stretch_and_bend_ik_nodes["handle"]
        length_end = self.stretch_and_bend_ik_nodes["length_end"]
        arm_control = self.controls["arm"]
        pm.parent(handle, length_end, arm_control)

        stretch_and_bend_ik_nodes = self.stretch_and_bend_ik_nodes.values()
        pm.hide(stretch_and_bend_ik_nodes)

        length_start = self.stretch_and_bend_ik_nodes["length_start"]
        length = self.stretch_and_bend_ik_nodes["length"]
        pm.parent(length_start, length, base_ik_const_group)

        if "right" == side:
            global_scale_node = self.stretch_and_bend_ik_nodes["scale"]
            name = "rightArm_inverse_DIV"
            inverse_node = pm.createNode("floatMath", n=name)
            inverse_node.operation.set(2)  # multiply
            inverse_node.floatB.set(-1)

            self.root_control.sx >> inverse_node.floatA
            inverse_node.outFloat >> global_scale_node.floatB

            sdks = global_scale_node.outFloat.outputs()
            for sdk in sdks:
                sdk.setPostInfinityType("constant")
                sdk.setPreInfinityType("linear")

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

        snap_start_loc = self.snap_nodes["locators"]["start"]
        snap_start_loc.setParent(base_ik_const_group)

        snap_length_nodes = self.snap_nodes["length"].values()
        pm.parent(snap_length_nodes, base_ik_const_group)

        if "right" == side:
            name = "rightArm_inverse_DIV"
            inverse_node = pm.PyNode(name)

            snap_scale_nodes = self.snap_nodes["scale"].values()
            for length_node in snap_scale_nodes:
                inverse_node.outFloat >> length_node.floatB

        snap_elbow_loc = self.snap_nodes["locators"]["snap"]
        for at in "trs":
            for ax in "xyz":
                pm.setAttr(snap_elbow_loc.attr(at + ax), lock=1, keyable=0)
        pm.setAttr(snap_elbow_loc.v, lock=1, keyable=0)

        # # add stretch attribute
        # elbow_stretch_choice = self.snap_nodes["stretch_blend"]
        # mid_sdk, = elbow_stretch_choice.color2R.inputs()
        # end_sdk, = elbow_stretch_choice.color2G.inputs()
        #
        # pm.addAttr(arm_control, ln="stretch", k=1, at="float", min=0, max=1)
        # ik_stretch_choice = \
        #     pm.createNode("blendColors", n=side + "Arm_IK_stretchChoice")
        #
        # arm_control.stretch >> ik_stretch_choice.blender
        # mid_sdk.output >> ik_stretch_choice.color1R
        # end_sdk.output >> ik_stretch_choice.color1G
        #
        # ik_stretch_choice.outputR >> elbow_stretch_choice.color2R
        # ik_stretch_choice.outputG >> elbow_stretch_choice.color2G
        #
        # ik_stretch_choice.color2R.set(ik_stretch_choice.color1R.get())
        # ik_stretch_choice.color2G.set(ik_stretch_choice.color1G.get())
        # ik_stretch_choice.color2B.set(0)

        # hybrid elbow
        hybrid_controls = self.hybrid_elbow(ik_const_group)
        ik_vis_group = self.hybrid_elbow_nodes["ik_vis"]
        ik_vis_group.setParent(arm_group)

        for at in "trs":
            for ax in "xyz":
                pm.setAttr(ik_vis_group.attr(at + ax), lock=1, keyable=0)
        pm.setAttr(ik_vis_group.v, lock=1, keyable=0)

        items = [v.getParent() for v in hybrid_controls.values()]
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, lock=1, keyable=0)

        items = hybrid_controls.values()
        for i in items:
            for at in "ts":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, lock=1, keyable=0)

        pm.setAttr(elbow_control.forearm_FK_visibility, l=1, k=0, cb=0)

        for k, v in hybrid_controls.items():
            self.controls["elbow_" + k] = v

        # SC solver for hand IK
        hand = self.ik_chain["hand"]
        end = self.ik_chain["end"]
        handle, effector = pm.ikHandle(sj=hand,
                                       ee=end,
                                       sol="ikSCsolver",
                                       n=side + "Hand_HDL")
        effector.rename(side + "Hand_EFF")
        handle.setParent(ik_const_group)
        handle.hide()

        items = [ik_const_group, base_ik_const_group]
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, lock=0, keyable=0, cb=1)
        ik_const_group.v.set(0)

        for ax in "xyz":
            pm.setAttr(arm_control.attr("s" + ax), lock=1, keyable=0)
        pm.setAttr(arm_control.v, keyable=0)

        for at in "rs":
            for ax in "xyz":
                pm.setAttr(elbow_control.attr(at + ax), lock=1, keyable=0)
        pm.setAttr(elbow_control.v, keyable=0, cb=0)
        return True

    @staticmethod
    def fk_rotation_space(spaces, driver=None, driven=None):
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
                st="*_{}Space_LOC*".format(dv))

            pm.setDrivenKeyframe(
                weight,
                currentDriver=driver,
                driverValue=rotation_space_values.index(dv),
                value=1,
                itt="auto",
                ott="step"
            )
        return orient_constraint

    def connect(self, controls):
        base_ik_const_group, fk_const_group, result_const_group = \
            [self.groups[k] for k in ["base_ik", "fk", "result"]]

        items = [fk_const_group, base_ik_const_group, result_const_group]
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=0)

        # spaces
        spaces = OrderedDict()  # shoulder = leftArm_shoulderSpace_LOC
        side = self.side
        innermost_space = None
        for i, con in enumerate(controls):
            name = con

            if side in str(con):
                # shoulder, body, root
                name = con.split(side)[1]

            key = name.split("_")[0].lower()
            name = side + "Arm_" + key + "Space_LOC"

            loc = pm.spaceLocator(n=name)
            pm.matchTransform(loc, self.result_chain["upper"], pos=1)
            pm.parent(loc, con)

            spaces[key] = loc

            if i == 0:
                # the inner most space drives IK and FK translation
                innermost_space = loc

        point_constraint = None
        for k in ["base_ik", "fk", "result"]:
            point_constraint = \
                pm.pointConstraint(innermost_space, self.groups[k])

        # FK rotation space
        arm_settings_con = self.controls["arm_settings"]
        pm.addAttr(arm_settings_con, ln="FK_rotationSpace", at="enum", k=1,
                   en=":".join(spaces.keys()))

        params = {
            "spaces": spaces,
            "driver": arm_settings_con.FK_rotationSpace,
            "driven": fk_const_group
        }
        self.fk_rotation_space(**params)

        # IKFK space switch blend
        name = side + "Arm"
        point_blend = \
            pm.createNode("blendColors", n=name + "_resultPointChoice")

        point_constraint.ctx // result_const_group.tx
        point_constraint.cty // result_const_group.ty
        point_constraint.ctz // result_const_group.tz

        arm_settings_con.FK_IK_blend >> point_blend.blender
        point_constraint.constraintTranslate >> point_blend.color1
        point_blend.color2.set(0, 0, 0)
        point_blend.output >> result_const_group.t

        # clean up
        items = spaces.values()
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, 0, lock=1, keyable=0,)

        items = [fk_const_group, base_ik_const_group, result_const_group]
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
        result_const_group.v.setKeyable(0)
        base_ik_const_group.v.set(0)
        return True
