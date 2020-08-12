import pymel.core as pm
from collections import OrderedDict


class Rig:
    def __init__(self, root, side="", root_control="", **kwargs):
        self.side = side
        self.root_control = root_control

        self.hand_loc = None
        for k, v in kwargs.items():
            if k == "hand_loc":
                self.hand_loc = pm.PyNode(v)

        name = "hand" if "" == side else side + "Hand"
        root.rename(name + "Base_result_JNT")
        self.result_chain = OrderedDict({"hand": root})

        self.groups = self._groups(side, root)
        self.controls = OrderedDict()

        self.palm_locators = OrderedDict()

        self.hand_locator = None
        self.constrain_joint = None

    def finger_chain(self, root, name="finger", orient=1):
        if orient:
            pm.joint(root, e=1, oj="xyz", sao="ydown", ch=1, zso=1)

        result_dict = OrderedDict()

        side = self.side
        n = name if "" == side else side + name.capitalize()
        root.rename(n + "Base_result_JNT")

        result_chain = [root] + root.getChildren(ad=1)[::-1]
        for i, jnt in enumerate(result_chain):
            jnt.rotateOrder.set(5)  # zyx

            if i == 0:
                result_dict["base"] = jnt
                continue

            jnt.rename("{}{}_result_JNT".format(n, i))
            result_dict[str(i)] = jnt

        if orient:
            result_chain[-1].jointOrient.set(0, 0, 0)
        pm.parent(root, self.result_chain["hand"])

        self.result_chain[name] = result_dict
        return result_dict

    def _groups(self, side, root):
        groups = OrderedDict()
        name = "hand" if "" == side else side + "Hand"

        groups["hand"] = hand = pm.group(em=1, n=name + "_GRP")

        groups["fk_const"] = fk_const = pm.group(em=1, n=name + "_FKConst_GRP")
        pm.matchTransform(fk_const, root, pos=1)
        fk_const.setParent(hand)

        groups["dont_touch"] = dont_touch = pm.group(em=1, n="dont_touch")
        dont_touch.setParent(hand)

        groups["const"] = const = pm.group(em=1, n=name + "_const_GRP")
        pm.matchTransform(const, root, piv=1)
        const.setParent(dont_touch)

        groups["handle"] = handle = pm.group(em=1, n=name + "_straightHDL_GRP")
        handle.setParent(const)
        return groups

    def finger_controls(self, finger_chain, name="finger"):
        controls = OrderedDict()

        tip_indicator = str(len(finger_chain) - 1)
        parent = None
        for k, v in finger_chain.items():
            n = v.split("result_JNT")[0]  # fingerBase_ or finger1_

            con = pm.spaceLocator(n=n + "CON")
            con.rotateOrder.set(5)  #zyx
            pm.matchTransform(con, v)

            sdk, = pm.duplicate(con, po=1, n=n + "SDK")
            ofs, = pm.duplicate(con, po=1, n=n + "OFS")

            pm.parent(con, sdk)
            pm.parent(sdk, ofs)
            pm.parent(ofs, parent)
            parent = con

            if tip_indicator == k:
                con.rename(con.replace("CON", "TIP"))
                ofs.hide()

            if "base" == k:
                con.rename(con.replace("CON", "ROOT"))
                pm.hide(con.getShapes())

            pm.parentConstraint(con, v, mo=1)

            _dict = {"ofs": ofs, "sdk": sdk, "con": con}
            controls[k] = _dict

        # detail attribute
        finger_control = controls["1"]["con"]
        pm.addAttr(finger_control, ln="conVis", nn="Secondary Controls",
                   at="bool", dv=0, k=0)
        pm.setAttr(finger_control.conVis, cb=1)

        for con in controls.values():
            if "CON" not in str(con["con"]):
                continue

            if "1" in str(con["con"]):
                continue

            if "Base" in str(con["con"]):
                continue

            finger_control.conVis >> con["ofs"].v

        # parent to fk const group
        first_control = controls.values()[0]
        pm.parent(first_control["ofs"], self.groups["fk_const"])

        self.controls[name] = controls
        return controls

    @staticmethod
    def flop(driver_con, sdk_null, attr="rz",
             min=-360, max=360, dmin=-50, dmax=95):
        pm.addAttr(driver_con, ln="flop", at="float", k=1, min=-10, max=10)

        name = driver_con + "_flop_SDK"
        sdk = pm.createNode("animCurveUL", n=name)

        pm.setKeyframe(sdk, f=0, v=0, itt="linear", ott="linear")
        pm.setKeyframe(sdk, f=10, v=max, itt="linear", ott="linear")
        pm.setKeyframe(sdk, f=-10, v=min, itt="linear", ott="linear")

        name = name.replace("SDK", "RMP")
        remap = pm.createNode("remapValue", n=name)
        remap.inputMin.set(min)
        remap.inputMax.set(max)

        driver_con.flop >> sdk.input
        sdk.output >> remap.inputValue
        remap.outValue >> sdk_null.attr(attr)

        range_nn = "Flop Range " + sdk_null
        pm.addAttr(driver_con, ln="flopRange", nn=range_nn, at="float2")
        pm.addAttr(driver_con, ln="flopMin", p="flopRange", at="float",
                   min=min, max=max, dv=dmin, k=0)
        pm.addAttr(driver_con, ln="flopMax", p="flopRange", at="float",
                   min=min, max=max, dv=dmax, k=0)

        remap.vl[0].vlp.set(0)
        driver_con.flopMin >> remap.vl[0].vlfv

        remap.vl[1].vlp.set(0.5)
        remap.vl[1].vlfv.set(0)

        remap.vl[2].vlp.set(1)
        driver_con.flopMax >> remap.vl[2].vlfv
        return True

    @staticmethod
    def curl(driver_con, sdk_nulls, attr="rz",
             min=-100, max=100, dmin=-20, dmax=95):
        pm.addAttr(driver_con, ln="curl", at="float", min=-10, max=10, k=1)
        name = driver_con + "_curl_SDK"
        sdk = pm.createNode("animCurveUL", n=name)

        pm.setKeyframe(sdk, f=0, v=0, itt="linear", ott="linear")
        pm.setKeyframe(sdk, f=10, v=max, itt="linear", ott="linear")
        pm.setKeyframe(sdk, f=-10, v=min, itt="linear", ott="linear")

        driver_con.curl >> sdk.input

        for i, sdk_null in enumerate(sdk_nulls):
            if not sdk_null:
                continue

            k = str(i + 1)
            range_name = "curlRange" + k
            range_nn = "Curl Range " + sdk_null
            min_name = "curlMin" + k
            max_name = "curlMax" + k

            pm.addAttr(driver_con, ln=range_name, nn=range_nn, at="float2")
            pm.addAttr(driver_con, ln=min_name, p=range_name, at="float",
                       min=min, max=max, dv=dmin, k=0)
            pm.addAttr(driver_con, ln=max_name, p=range_name, at="float",
                       min=min, max=max, dv=dmax, k=0)

            name = sdk_null.replace("SDK", "RMP")
            remap = pm.createNode("remapValue", n=name)
            remap.inputMin.set(min)
            remap.inputMax.set(max)

            sdk.output >> remap.inputValue
            remap.outValue >> sdk_null.attr(attr)

            remap.vl[0].vlp.set(0)
            driver_con.attr(min_name) >> remap.vl[0].vlfv

            remap.vl[1].vlp.set(0.5)
            remap.vl[1].vlfv.set(0)

            remap.vl[2].vlp.set(1)
            driver_con.attr(max_name) >> remap.vl[2].vlfv
        return True

    @staticmethod
    def lean(finger_controls, attr="ry",
             min=-100, max=100, dmin=-20, dmax=20):
        first = finger_controls["1"]  # metacarpophalangeal
        first_con = first["con"]
        first_sdk = first["sdk"]

        pm.addAttr(first_con, ln="lean", at="float", k=1, min=-10, max=10)

        name = first_con + "_lean_SDK"
        sdk = pm.createNode("animCurveUL", n=name)

        pm.setKeyframe(sdk, f=0, v=0, itt="linear", ott="linear")
        pm.setKeyframe(sdk, f=10, v=max, itt="linear", ott="linear")
        pm.setKeyframe(sdk, f=-10, v=min, itt="linear", ott="linear")

        name = name.replace("SDK", "RMP")
        remap = pm.createNode("remapValue", n=name)
        remap.inputMin.set(min)
        remap.inputMax.set(max)

        first_con.lean >> sdk.input
        sdk.output >> remap.inputValue
        remap.outValue >> first_sdk.attr(attr)

        range_nn = "Lean Range " + first["sdk"]
        pm.addAttr(first_con, ln="leanRange", nn=range_nn, at="float2")
        pm.addAttr(first_con, ln="leanMin", p="leanRange", at="float",
                   min=min, max=max, dv=dmin, k=0)
        pm.addAttr(first_con, ln="leanMax", p="leanRange", at="float",
                   min=min, max=max, dv=dmax, k=0)

        remap.vl[0].vlp.set(0)
        first_con.leanMin >> remap.vl[0].vlfv

        remap.vl[1].vlp.set(0.5)
        remap.vl[1].vlfv.set(0)

        remap.vl[2].vlp.set(1)
        first_con.leanMax >> remap.vl[2].vlfv
        return True

    @staticmethod
    def spread(finger_controls, attr="ry",
               min=-100, max=100, dmin=-20, dmax=20):
        first = finger_controls["1"]  # carpometacarpal
        first_con = first["con"]
        base_sdk = finger_controls["base"]["sdk"]

        pm.addAttr(first_con, ln="spread", at="float", k=1, min=-10, max=10)

        name = first_con + "_spread_SDK"
        sdk = pm.createNode("animCurveUL", n=name)

        pm.setKeyframe(sdk, f=0, v=0, itt="linear", ott="linear")
        pm.setKeyframe(sdk, f=10, v=max, itt="linear", ott="linear")
        pm.setKeyframe(sdk, f=-10, v=min, itt="linear", ott="linear")

        name = name.replace("SDK", "RMP")
        remap = pm.createNode("remapValue", n=name)
        remap.inputMin.set(min)
        remap.inputMax.set(max)

        first_con.spread >> sdk.input
        sdk.output >> remap.inputValue
        remap.outValue >> base_sdk.attr(attr)

        range_nn = "Spread Range " + base_sdk
        pm.addAttr(first_con, ln="spreadRange", nn=range_nn, at="float2")
        pm.addAttr(first_con, ln="spreadMin", p="spreadRange", at="float",
                   min=min, max=max, dv=dmin, k=0)
        pm.addAttr(first_con, ln="spreadMax", p="spreadRange", at="float",
                   min=min, max=max, dv=dmax, k=0)

        remap.vl[0].vlp.set(0)
        first_con.spreadMin >> remap.vl[0].vlfv

        remap.vl[1].vlp.set(0.5)
        remap.vl[1].vlfv.set(0)

        remap.vl[2].vlp.set(1)
        first_con.spreadMax >> remap.vl[2].vlfv
        return True

    @staticmethod
    def length(driver, driven_objs):
        pm.addAttr(driver, ln="length", at="float", k=1, min=0, dv=1)

        for driven in driven_objs:
            value = driven["ofs"].tx.get() * -1
            name = driven["con"] + "_length_SDK"
            driven = driven["sdk"].tx

            sdk = pm.createNode("animCurveUL", n=name)
            pm.setKeyframe(sdk, f=1, v=0, itt="spline", ott="spline")
            pm.setKeyframe(sdk, f=0, v=value)
            sdk.postInfinity.set(1)  # linear

            driver.length >> sdk.input
            sdk.output >> driven
        return True

    def finger_attributes(self, fingers=[]):
        spread = {
            "index": {"dmin": -2, "dmax": 10},
            "middle": {"dmin": 0, "dmax": 0},
            "ring": {"dmin": 2, "dmax": -10},
            "pinky": {"dmin": 2, "dmax": -25}
        }

        for name in fingers:
            finger_chain = self.result_chain[name]
            finger_controls = self.finger_controls(finger_chain, name=name)

            driver_con = finger_controls["1"]["con"]
            sdk_null = finger_controls["1"]["sdk"]
            sdk_nulls = [v["sdk"] for v in finger_controls.values()[2:-1]]

            if "thumb" == name:
                self.flop(driver_con, sdk_null, dmin=-20, dmax=70)
                self.curl(driver_con, sdk_nulls, dmin=-20, dmax=60)
            else:
                self.flop(driver_con, sdk_null)
                self.curl(driver_con, sdk_nulls)
                self.spread(finger_controls, **spread[name])
                self.lean(finger_controls)

            if "pinky" == name:
                driver_con.leanMin.set(-50)

            driven_objs = [v for v in finger_controls.values()[2:]]
            self.length(driver_con, driven_objs)
        return True

    def palm_raise(self):
        driver = self.controls["hand"]["con"]
        driven = self.palm_locators["middle"].rz

        pm.addAttr(driver, ln="palmRaise", at="float", min=-90, max=90, k=1)
        pm.setDrivenKeyframe(driven,
                             cd=driver.palmRaise, dv=-90, v=90,
                             itt="linear", ott="linear")
        pm.setDrivenKeyframe(driven,
                             cd=driver.palmRaise, dv=90, v=-90,
                             itt="linear", ott="linear")
        return True

    def palm_side_roll(self):
        driver = self.controls["hand"]["con"]
        pm.addAttr(driver, ln="sideRoll", at="float", min=-90, max=90, k=1)

        driven = self.palm_locators["inner"].rx
        pm.setDrivenKeyframe(driven,
                             cd=driver.sideRoll, dv=-90, v=90,
                             itt="linear", ott="linear")
        pm.setDrivenKeyframe(driven,
                             cd=driver.sideRoll, dv=0, v=0,
                             itt="linear", ott="linear")

        driven = self.palm_locators["outer"].rx
        pm.setDrivenKeyframe(driven,
                             cd=driver.sideRoll, dv=0, v=0,
                             itt="linear", ott="linear")
        pm.setDrivenKeyframe(driven,
                             cd=driver.sideRoll, dv=90, v=-90,
                             itt="linear", ott="linear")
        return True

    def finger_ik(self, name):
        side = self.side
        finger_chain = self.result_chain[name]

        n = name + "_straightStart_JNT"
        start_name = n if "" == side else side + n[0].upper() + n[1:]
        finger_chain_root = finger_chain["1"]
        start_joint, = pm.duplicate(finger_chain_root, n=start_name, po=1)

        pm.parent(finger_chain["1"], start_joint)

        n = name + "_straightEnd_JNT"
        end_name = n if "" == side else side + n[0].upper() + n[1:]
        finger_chain_tip = finger_chain.values()[-1]
        end_joint, = pm.duplicate(finger_chain_tip, n=end_name, po=1)

        pm.parent(end_joint, start_joint)

        n = name + "_straight_HDL"
        handle_name = n if "" == side else side + n[0].upper() + n[1:]
        handle, effector = pm.ikHandle(sj=start_joint,
                                       ee=end_joint,
                                       sol="ikSCsolver",
                                       n=handle_name)
        effector.rename(handle_name.replace("HDL", "EFF"))

        handle.setParent(self.groups["handle"])
        start_joint.drawStyle.set(2)  # None - bone is "hidden"
        end_joint.drawStyle.set(2)
        return start_joint, handle

    def palm_attributes(self, palm, fingers=[]):
        side = self.side
        name = "hand" if "" == side else side + "Hand"

        # leftHand_CON
        hand_control = pm.spaceLocator(n=name + "_CON")
        try:
            pm.matchTransform(hand_control, self.hand_loc)
        except:
            pm.matchTransform(hand_control, self.result_chain["hand"], pos=1)
            hand_control.ty.set(hand_control.ty.get() + 10)

        ofs, = pm.duplicate(hand_control, po=1, n=name + "_OFS")
        hand_control.setParent(ofs)
        ofs.setParent(self.groups["hand"])

        self.controls["hand"] = {"ofs": ofs, "con": hand_control}

        middle, inner, outer = palm

        # palm locators and constrain joint
        self.palm_locators["inner"] = inner
        self.palm_locators["outer"] = outer
        self.palm_locators["middle"] = middle

        parent = None
        for k, v in self.palm_locators.items():
            n = k + "Palm_LOC"
            n = n if "" == side else "_".join([side, n])
            v.rename(n)

            pm.parent(v, parent)
            parent = v

        name = "hand_baseConst_JNT"
        name = name if "" == side else side + name[0].upper() + name[1:]
        const_joint, = pm.duplicate(self.result_chain["hand"], po=1, n=name)
        const_joint.setParent(self.palm_locators["middle"])
        self.constrain_joint = const_joint

        self.palm_locators["inner"].setParent(self.groups["const"])
        pm.parentConstraint(const_joint, self.groups["fk_const"], mo=1)
        pm.parentConstraint(const_joint, self.result_chain["hand"], mo=1)
        pm.parentConstraint(const_joint, ofs, mo=1)

        for name in fingers:
            straight_start_joint, straight_handle = self.finger_ik(name)
            offset = self.controls[name]["1"]["ofs"]
            pm.parentConstraint(straight_start_joint, offset, mo=1)

        self.palm_raise()
        if "right" == side:
            name = "rightHand_inverse_DIV"
            inverse_node = pm.createNode("floatMath", n=name)
            inverse_node.operation.set(2)  # multiply
            inverse_node.floatB.set(-1)

            palm_raise_sdk = hand_control.palmRaise.outputs()[0]
            hand_control.palmRaise >> inverse_node.floatA
            inverse_node.outFloat >> palm_raise_sdk.input

        self.palm_side_roll()
        return const_joint

    def connect(self, control=None, bind_joint=None, settings=None):
        self.result_chain["hand"].setParent(self.groups["dont_touch"])
        self.groups["hand"].setParent(self.root_control)
        self.groups["const"].hide()

        side = self.side
        name = "hand" if "" == side else side + "Hand"
        hand_loc = pm.spaceLocator(n=name + "_LOC")

        pm.matchTransform(hand_loc, self.groups["const"])
        pm.parentConstraint(hand_loc, self.groups["const"])

        if control:
            pm.parent(hand_loc, control)

        if bind_joint:
            pm.delete(bind_joint.inputs()[0])
            pm.parentConstraint(self.constrain_joint, bind_joint, mo=1)

        if settings:
            pm.addAttr(settings, ln="hand_fk_visibility",
                       k=1, at="bool", dv=1)
            settings.hand_fk_visibility >> self.groups["fk_const"].v

            pm.addAttr(settings, ln="hand_con_visibility",
                       k=1, at="bool", dv=1)
            settings.hand_con_visibility >> self.controls["hand"]["ofs"].v

        lock_and_hide_all = []
        lock_and_hide_all_except_rotate = []
        for name, finger_chain in self.controls.items()[:-1]:  # skips hand
            for knuckles in finger_chain.values():
                ofs, con, sdk = knuckles.values()
                if sdk:
                    lock_and_hide_all += [sdk]
                if ofs:
                    lock_and_hide_all += [ofs]
                if "TIP" in con:
                    lock_and_hide_all += [con]
                else:
                    lock_and_hide_all_except_rotate += [con]

        items = [self.controls["hand"][k] for k in ["ofs", "con"]]
        items += lock_and_hide_all
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, lock=1, keyable=0)

        items = lock_and_hide_all_except_rotate
        for i in items:
            for at in "ts":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, lock=1, keyable=0)

        items = self.groups.values()
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, lock=0, keyable=0, cb=1)

        pm.hide(self.groups["const"], self.groups["handle"], hand_loc)
        return hand_loc, self.constrain_joint
