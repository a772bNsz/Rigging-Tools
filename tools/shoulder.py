import pymel.core as pm
from collections import OrderedDict


class Rig:
    def __init__(self, root, side="", root_control=""):
        self.side = side
        self.root_control = root_control

        self.result_chain = OrderedDict({"root": root})
        self.result_chain["end"] = root.getChildren(type="joint")[0]

        self.result_chain["root"].rename(side + "ShoulderBase_result_JNT")
        self.result_chain["end"].rename(side + "ShoulderEnd_result_JNT")

        self.groups = self._groups(side)
        self.controls = self._controls()
        self.ik_nodes = {}
        self.stretch_ik_nodes = {}
        self.connect_nodes = {}

    def _groups(self, side):
        groups = OrderedDict(
            {"shoulder": pm.group(em=1, n=side + "Shoulder_GRP")})
        groups["dont_touch"] = pm.group(em=1, n="dontTouch_GRP")

        groups["attach"] = pm.group(em=1, n=side + "Shoulder_attach_GRP")

        pm.parent(groups["dont_touch"], groups["shoulder"])
        pm.parent(self.result_chain["root"], groups["dont_touch"])

        items = [groups["dont_touch"]]
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, keyable=0, cb=1)
        return groups

    def _controls(self, translate=1, rotate=0):
        side = self.side
        controls = {
            "shoulder": None
        }

        if translate:
            # translation based control
            con = pm.spaceLocator(n=side + "Shoulder_CON")
            ofs = pm.group(n=side + "Shoulder_OFS")

            pm.matchTransform(ofs, self.result_chain["end"], pos=1)
            controls["shoulder"] = con

        if rotate:
            pass

        i = controls["shoulder"]
        for at in "rs":
            for ax in "xyz":
                pm.setAttr(i.attr(at + ax), lock=1, keyable=0)

        i = controls["shoulder"].getParent()
        for at in "trs":
            for ax in "xyz":
                pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
        pm.setAttr(i.v, lock=1, keyable=0)

        pm.parent(controls["shoulder"].getParent(), self.groups["shoulder"])
        return controls

    def stretch_ik(self, handle, start, end, name):
        # IK stretches beyond default length
        length_start = pm.spaceLocator(n=name + "_IK_lengthStart_LOC")
        length_end = pm.spaceLocator(n=name + "_IK_lengthEnd_LOC")

        pm.matchTransform(length_start, start, pos=1)
        pm.matchTransform(length_end, end, pos=1)

        length = pm.distanceDimension(
            sp=length_start.worldPosition.get(),
            ep=length_end.worldPosition.get()).getParent()
        length.rename(name + "_IK_length")

        # SDK
        natural_length = end.tx.get()
        distance_length = length.distance.get()

        pm.setDrivenKeyframe(end.tx,
                             cd=length.distance,
                             dv=distance_length,
                             v=natural_length)
        pm.setDrivenKeyframe(end.tx,
                             cd=length.distance,
                             dv=distance_length * 2,
                             v=natural_length * 2)
        pm.setInfinity(end.tx, poi="linear")

        # global scale
        n = "_".join(["globalScale", name, "normalize_DIV"])
        global_scale = pm.createNode("floatMath", n=n)
        global_scale.operation.set(3)

        end_sdk = end.tx.inputs()[0]
        length.distance >> global_scale.floatA
        self.root_control.sx >> global_scale.floatB
        global_scale.outFloat >> end_sdk.input

        # cleanup
        pm.hide(handle, length_start, length_end, length)

        self.stretch_ik_nodes = {
            "length": length,
            "length_start": length_start,
            "length_end": length_end,
            "globalScale": global_scale
        }

        pm.parent(length, length_start, self.groups["dont_touch"])
        return self.stretch_ik_nodes

    def ik(self):
        side = self.side
        name = side + "Shoulder"
        start = self.result_chain["root"]
        end = self.result_chain["end"]
        shoulder_con = self.controls["shoulder"]

        # single-chain IK handle
        handle, effector = pm.ikHandle(sj=start, ee=end, sol="ikSCsolver")
        handle.rename(name + "_HDL")
        effector.rename(name + "_EFF")

        locator = pm.spaceLocator(n=name + "_LOC")
        pm.matchTransform(locator, end, pos=1)

        pm.parent(handle, locator)
        pm.parent(locator, shoulder_con)
        pm.hide(locator)

        for at in "rs":
            for ax in "xyz":
                pm.setAttr(shoulder_con.attr(at + ax), lock=1, keyable=0)
        pm.setAttr(shoulder_con.v, lock=1, keyable=0,)

        # prep abstraction receiver
        attach_group = self.groups["attach"]
        pm.parentConstraint(end, attach_group)
        pm.parent(attach_group, self.controls["shoulder"])

        i = attach_group
        for at in "trs":
            for ax in "xyz":
                pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
        pm.setAttr(i.v, lock=1, keyable=0)

        self.ik_nodes = {
            "handle": handle,
            "abstraction_locator": locator
        }

        self.stretch_ik(handle, start, end, name)
        self.stretch_ik_nodes["length_end"].setParent(locator)
        return self.ik_nodes

    def connect(self, name="shoulder", control=None):
        n = name if "" == self.side else self.side + "Shoulder"
        const_loc = pm.spaceLocator(n=n + "_const_LOC")

        shoulder_grp = self.groups[name]
        pm.matchTransform(const_loc, self.controls[name])
        constraint_node = \
            pm.parentConstraint(const_loc, shoulder_grp, mo=1)

        pm.parent(const_loc, control)
        const_loc.hide()
        pm.select(cl=1)

        items = [shoulder_grp]
        for i in items:
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i.v, keyable=0, cb=1)

        self.connect_nodes = {
            "abstraction_locator": const_loc,
            "parent_constraint": constraint_node
        }
        return self.connect_nodes
