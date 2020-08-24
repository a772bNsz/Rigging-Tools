import pymel.core as pm
from os import path


class Rig:
    def __init__(self):
        print ">> attaching cartoony bezier rig"

    @staticmethod
    def import_maya_files(filenames=[]):
        maya_dir = path.join(path.dirname(__file__), "ma")
        for name in filenames:
            maya_file = path.join(maya_dir, name + ".ma")
            pm.importFile(maya_file, f=1, ra=1, namespace=":")
        return True

    def _rename_node(self, source, node, children=0):
        root = source.split("_", 1)[0]

        new_name = "_".join([root, node])
        node = pm.PyNode(node)
        node.rename(new_name)

        if children:
            nodes = node.getChildren(ad=1)
            for n in nodes:
                new_name = "_".join([root, str(n)])
                n.rename(new_name)
        return node

    def connect(self, start, middle, end, root=None):
        # connecting to start
        pm.delete("upper_start_parentConstraint1")
        cartoony_start = self._rename_node(start, "upper_start")

        pm.matchTransform(cartoony_start, start, pos=1)
        pm.parentConstraint(start, cartoony_start, mo=1)

        # connecting to end
        pm.delete("lower_end_parentConstraint1")
        cartoony_end = self._rename_node(end, "lower_end")

        pm.matchTransform(cartoony_end, end, pos=1)
        pm.parentConstraint(end, cartoony_end, mo=1)

        # connecting to middle
        cartoony_mid = self._rename_node(middle, "bezier_OFS", children=1)

        aim = pm.PyNode("aim_LOC")
        upv = pm.PyNode("upv_LOC")
        crv = pm.PyNode("curve1")
        point_on_curve_node = self._rename_node(middle, "test_poc_010")

        bezier_aim_start = pm.PyNode("start_GRP")
        bezier_aim_end = pm.PyNode("end_GRP")

        pm.delete("start_GRP_parentConstraint1", "end_GRP_parentConstraint1")
        bezier_aim_group = \
            self._rename_node(middle, "bezier_aim_GRP", children=1)

        pm.matchTransform(bezier_aim_start, start, pos=1)
        pm.parentConstraint(start, bezier_aim_start, mo=1)

        pm.matchTransform(bezier_aim_end, end, pos=1)
        pm.parentConstraint(end, bezier_aim_end, mo=1)

        # this method only works if the arm chain is straight!
        # the length of the entire arm comes from the translate x values
        # of the forearm and the hand
        # "end" is the hand joint in the hand group
        # and not the hand joint in the arm group
        # so the translate x you'd get on the hand joint does nothing for you
        # using listRelatives on forearm to get the hand joint tx we want
        value = abs(pm.listRelatives(middle)[0].tx.get() / crv.length())
        point_on_curve_node.parameter.set(value)

        pm.matchTransform(upv, middle, pos=1)
        pm.move(3, upv, y=1, ws=1, r=1)

        pm.parentConstraint(middle, upv, mo=1)
        pm.pointConstraint(middle, cartoony_mid)

        # this if statement is only for this sketch
        # the bezier aim should be in front of the bezier in world space z
        # it is not because the start and end are reversed,
        # thus the rivet is reversed
        # in a later draft, the cv order of the curve will correspond with
        # the start and end param
        if cartoony_mid.startswith("right"):
            pm.move(6, aim, z=1, ws=1, r=1)
        pm.aimConstraint(aim, cartoony_mid, mo=1,
                         aim=[1, 0, 0],
                         u=[0, 0, 1],
                         wut="objectrotation",
                         wuo=upv,
                         wu=[0, 1, 0])

        # clean up
        upper_seg_joints = pm.listRelatives("upper_GRP", ad=1, type="joint")
        for jnt in upper_seg_joints:
            self._rename_node(start, str(jnt))
        self._rename_node(start, "upper_GRP")

        lower_seg_joints = pm.listRelatives("lower_GRP", ad=1, type="joint")
        for jnt in lower_seg_joints:
            self._rename_node(start, str(jnt))
        self._rename_node(middle, "lower_GRP")

        if root:
            joints = upper_seg_joints + lower_seg_joints
            for jnt in joints:
                pm.scaleConstraint(root, jnt, mo=1)

        pm.parent(cartoony_mid, None)
        pm.delete("controls", "pCylinder1")

        bezier_aim_group.setParent("cartoony_GRP")

        update_auto_rig_arm = \
            "result" in start and "result" in middle and "baseConst" in end

        if update_auto_rig_arm:
            side = "left" if start.startswith("left") else "right"
            self._update_auto_rig_arm(side, cartoony_mid)

        pm.select(cl=1)
        return True

    def _update_auto_rig_arm(self, side, bezier_control):
        arm_group = side + "Arm_GRP"
        cartoony_group = self._rename_node(arm_group, "cartoony_GRP")

        dont_touch = "|".join([arm_group, "dontTouch_GRP"])
        cartoony_group.setParent(dont_touch)

        pm.parent(bezier_control, arm_group)

        twist_group = arm_group.replace("_", "_twist_")
        pm.delete("group1", twist_group)
        cartoony_group.hide()
        return True
