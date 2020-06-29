import pymel.core as pm
from collections import OrderedDict


class Rig:
    def __init__(self, root, side=""):
        self.side = side

        self.result_chain = OrderedDict({"root": root})
        self.result_chain["end"] = root.getChildren(type="joint")[0]

        self.result_chain["root"].rename(side + "ShoulderBase_result_JNT")
        self.result_chain["end"].rename(side + "ShoulderEnd_result_JNT")

        self.controls = self._controls()
        self.ik_nodes = {}
        self.stretch_ik_nodes = {}

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

        natural_length = end.tx.get()
        distance_length = length.distance.get()

        # --- SDK
        pm.setDrivenKeyframe(end.tx,
                             cd=length.distance,
                             dv=distance_length,
                             v=natural_length)
        pm.setDrivenKeyframe(end.tx,
                             cd=length.distance,
                             dv=distance_length * 2,
                             v=natural_length * 2)
        pm.setInfinity(end.tx, poi="linear")

        # cleanup
        pm.hide(handle, length_start, length_end, length)

        self.stretch_ik_nodes = {
            "length": length,
            "length_start": length_start,
            "length_end": length_end
        }
        return self.stretch_ik_nodes

    def ik(self):
        side = self.side
        name = side + "Shoulder"
        start = self.result_chain["root"]
        end = self.result_chain["end"]

        # single-chain IK handle
        handle, effector = pm.ikHandle(sj=start, ee=end, sol="ikSCsolver")
        handle.rename(name + "_HDL")
        effector.rename(name + "_EFF")

        locator = pm.spaceLocator(n=side + name + "_LOC")
        pm.matchTransform(locator, end, pos=1)

        pm.parent(handle, locator)
        pm.parent(locator, self.controls["shoulder"])
        pm.hide(locator)

        self.ik_nodes = {
            "handle": handle,
            "abstraction_locator": locator
        }

        self.stretch_ik(handle, start, end, name)
        self.stretch_ik_nodes["length_end"].setParent(locator)
        return self.ik_nodes
