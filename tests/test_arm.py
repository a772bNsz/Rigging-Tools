import unittest
import pymel.core as pm
from tools.arm import Rig
from tests.test_shoulder import TestShoulder


class TestArm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"

    def setUp(self):
        pm.newFile(f=1)

        self.controls = ["leftShoulder_CON", "body_CON", "root_transform_CON"]

        parent = None
        for i in range(3)[::-1]:
            name = self.controls[i]
            con = pm.spaceLocator(n=name)
            con.setParent(parent)
            self.controls[i] = parent = con

        pm.move(self.controls[1], [0.0, 91.23, -0.45], a=1)
        pm.move(self.controls[0], [17.19, 138.49, 0.93], a=1)

        pm.select(cl=1)

        root = pm.joint(p=[17.19, 138.49, 0.94], a=1)
        pm.joint(p=[40.69, 138.49, 1.44], a=1)
        pm.joint(p=[68.17, 138.49, 2.02], a=1)
        pm.joint(p=[75.66, 138.49, 2.18], a=1)

        root_con = self.controls[-1]

        self.arm = Rig(root, side="left", root_control=root_con)

    @unittest.skip("")
    def test_arm_with_twist(self):
        arm = self.arm
        arm.twist()
        arm.ikfk_switch()
        arm.fk()
        arm.ik()
        arm.connect()
        self.assertTrue(len(arm.controls) == 9,
                        "arm rig with failed")

    # @unittest.skip("")
    def test_connect(self):
        arm = self.arm
        arm.twist()
        arm.ikfk_switch()
        arm.fk()
        arm.ik()

        controls = self.controls
        # ["leftShoulder_CON", "body_CON", "root_transform_CON"]
        spaces = arm.connect(controls)
        self.assertTrue(spaces,
                        "connection failed")

    @unittest.skip("")
    def test_ikfk_switch(self):
        arm = self.arm
        blend_nodes = arm.ikfk_switch()
        self.assertTrue(blend_nodes,
                        "did not create IK/FK switch")

    @unittest.skip("")
    def test_fk_arm(self):
        arm = self.arm
        arm.ikfk_switch()
        fk_controls = arm.fk()
        self.assertTrue(fk_controls,
                        "did not create fk arm")

    @unittest.skip("")
    def test_create_twist_chain(self):
        arm = self.arm
        params = {
            "curve": pm.curve(d=1, p=[[0, 0, 0], [5, 0, 0]], k=[0, 1]),
            "number": 5,
            "name": "leftUpperArm_seg#_JNT"
        }
        chain = arm.create_twist_chain(**params)
        self.assertTrue(chain,
                        "failed to create upper arm twist chain")

    @unittest.skip("")
    def test_ik_spline(self):
        arm = self.arm
        side = arm.side
        name = side + "UpperArm"
        curve = pm.curve(d=1,
                         p=[[17.19, 138.49, 0.94], [40.69, 138.49, 1.44]],
                         k=[0, 1],
                         n=name + "_CRV")
        params = {
            "curve": curve,
            "name": name + "_seg#_JNT"
        }
        chain = arm.create_twist_chain(**params)

        params = {
            "oj": "xyz",  # joint orientation
            "sao": "ydown",  # secondary axis orientation
            "up_axis": 3,  # +z
            "up_vectors": [[0, 0, 1]] * 2,
            "curve": curve,
            "chain": chain,
            "name": name,
        }
        twisted = arm.ik_spline(**params)
        twisted["start_bind"].rename(side + "Arm_start_bind_JNT")
        twisted["end_bind"].rename(side + "Arm_mid_bind_JNT")
        self.assertTrue(arm.twist_nodes,
                        "upper arm twist failed")

    @unittest.skip("")
    def test_ik_spline_stretch(self):
        arm = self.arm
        side = arm.side

        # twist chain
        name = side + "UpperArm"
        curve = pm.curve(d=1,
                         p=[[17.19, 138.49, 0.94], [40.69, 138.49, 1.44]],
                         k=[0, 1],
                         n=name + "_CRV")
        params = {
            "curve": curve,
            "name": name + "_seg#_JNT"
        }
        chain = arm.create_twist_chain(**params)

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
        twisted = arm.ik_spline(**params)
        twisted["start_bind"].rename(side + "Arm_start_bind_JNT")
        twisted["end_bind"].rename(side + "Arm_mid_bind_JNT")

        # stretch
        params = {
            "curve": curve,
            "chain": chain,
            "control": arm.root_control.sx,
            "name": name,
        }
        stretched = arm.stretch_spline(**params)
        self.assertTrue(stretched,
                        "upper and lower arm stretch failed")

    @unittest.skip("")
    def test_upper_lower_twist(self):
        arm = self.arm
        side = arm.side

        twist_group = pm.group(em=1, n=side + "Arm_twist_GRP")
        arm.twist_nodes["twist_group"] = twist_group
        upperarm_twisted = arm._twist_upperarm()
        lowerarm_twisted = arm._twist_lowerarm()
        self.assertTrue(upperarm_twisted and lowerarm_twisted,
                        "twist on upper and lower arm failed")

    @unittest.skip("")
    def test_connect_twist_to_result_chain(self):
        arm = self.arm
        arm.twist()
        self.assertTrue(arm.ikfk_switch(),
                        "failed to connect twist chains to result chain")

    @unittest.skip("")
    def test_stretch_and_bend_ik(self):
        arm = self.arm
        side = arm.side
        name = side + "Arm"

        # RP solver
        start, mid, end = [v for v in arm.ik_chain.values()[:-1]]

        mid.r.set([0, 10, 0])
        mid.setPreferredAngles()
        mid.r.set(0, 0, 0)

        handle, effector = pm.ikHandle(sj=start, ee=end, sol="ikRPsolver")
        handle.rename(name + "HDL")
        effector.rename(name + "EFF")

        # stretch and bend IK
        params = {
            "name": name,
            "joints": [start, mid, end],
            "handle": handle
        }
        arm.stretch_and_bend_ik(**params)

        handle = arm.stretch_and_bend_ik_nodes["handle"]
        length_end = arm.stretch_and_bend_ik_nodes["length_end"]
        arm_control = arm.controls["arm"]
        stretch_and_bend_ik_nodes = arm.stretch_and_bend_ik_nodes.values()

        pm.parent(handle, length_end, arm_control)
        pm.hide(stretch_and_bend_ik_nodes)
        self.assertTrue(arm.stretch_and_bend_ik_nodes,
                        "failed to stretch and bend IK rp solver arm")

    @unittest.skip("")
    def test_elbow_snap(self):
        arm = self.arm
        side = arm.side
        name = side + "Arm"

        # RP solver
        start, mid, end = [v for v in arm.ik_chain.values()[:-1]]

        mid.r.set([0, 10, 0])
        mid.setPreferredAngles()
        mid.r.set(0, 0, 0)

        handle, effector = pm.ikHandle(sj=start, ee=end, sol="ikRPsolver")
        handle.rename(name + "HDL")
        effector.rename(name + "EFF")

        # stretch and bend IK
        params = {
            "name": name,
            "joints": [start, mid, end],
            "handle": handle
        }
        arm.stretch_and_bend_ik(**params)

        handle = arm.stretch_and_bend_ik_nodes["handle"]
        length_end = arm.stretch_and_bend_ik_nodes["length_end"]
        arm_control = arm.controls["arm"]
        stretch_and_bend_ik_nodes = arm.stretch_and_bend_ik_nodes.values()

        pm.parent(handle, length_end, arm_control)
        pm.hide(stretch_and_bend_ik_nodes)

        # snappable elbow
        params = {
            "controls": {
                "snap": arm.controls["elbow"],
                "main": arm.controls["arm"],
                "attr": "elbowSnap"
            },
            "locators": {
                "snap": side + "Elbow_LOC",
                "start": side + "UpperArm_to_elbowDistStart_LOC",
                "end": side + "Elbow_to_handDistEnd_LOC"
            },
            "joints": [v for v in arm.ik_chain.values()[:-1]],
            "length": {
                "first": side + "UpperArm_to_elbow_distance",
                "second": side + "Elbow_to_hand_distance"
            },
            "handle": handle,
            "stretch_blend": side + "Elbow_stretchChoice"
        }
        arm.snap(**params)

        for k in ["locators", "length"]:
            pm.hide(arm.snap_nodes[k].values())

        self.assertTrue(arm.snap_nodes,
                        "snappable elbow failed")

    @unittest.skip("")
    def test_hybrid_elbow(self):
        arm = self.arm
        side = arm.side
        name = side + "Arm"

        arm.ikfk_switch()

        # RP solver
        start, mid, end = [v for v in arm.ik_chain.values()[:-1]]

        mid.r.set([0, 10, 0])
        mid.setPreferredAngles()
        mid.r.set(0, 0, 0)

        handle, effector = pm.ikHandle(sj=start, ee=end, sol="ikRPsolver")
        handle.rename(name + "HDL")
        effector.rename(name + "EFF")

        # stretch and bend IK
        params = {
            "name": name,
            "joints": [start, mid, end],
            "handle": handle
        }
        arm.stretch_and_bend_ik(**params)

        handle = arm.stretch_and_bend_ik_nodes["handle"]
        length_end = arm.stretch_and_bend_ik_nodes["length_end"]
        arm_control = arm.controls["arm"]
        stretch_and_bend_ik_nodes = arm.stretch_and_bend_ik_nodes.values()

        pm.parent(handle, length_end, arm_control)
        pm.hide(stretch_and_bend_ik_nodes)

        # snappable elbow
        params = {
            "controls": {
                "snap": arm.controls["elbow"],
                "main": arm.controls["arm"],
                "attr": "elbowSnap"
            },
            "locators": {
                "snap": side + "Elbow_LOC",
                "start": side + "UpperArm_to_elbowDistStart_LOC",
                "end": side + "Elbow_to_handDistEnd_LOC"
            },
            "joints": [v for v in arm.ik_chain.values()[:-1]],
            "length": {
                "first": side + "UpperArm_to_elbow_distance",
                "second": side + "Elbow_to_hand_distance"
            },
            "handle": handle,
            "stretch_blend": side + "Elbow_stretchChoice"
        }
        arm.snap(**params)

        for k in ["locators", "length"]:
            pm.hide(arm.snap_nodes[k].values())

        ik_const_group = arm.groups["ik"]
        arm.hybrid_elbow(ik_const_group)
        self.assertTrue(arm.hybrid_elbow_nodes,
                        "hybrid elbow failed")

    @unittest.skip("")
    def test_ik(self):
        arm = self.arm

        arm.ikfk_switch()
        ik_controls = arm.ik()
        self.assertTrue(ik_controls,
                        "ik set up failed")

    @classmethod
    def tearDownClass(cls):
        try:
            from tools.control_shapes import ControlShapes
            json_file = __file__.split("tests")[0] + "/results/arm.json"
            cs = ControlShapes()
            cs.load(json_file=json_file)
        except:
            pass
        pm.saveAs("result.ma", type="mayaAscii")
        print ">>>>> TEARDOWN"


class TestShoulderArmConnection(TestShoulder):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"

    def setUp(self):
        pm.newFile(f=1)
        super(TestShoulderArmConnection, self).setUp()
        super(TestShoulderArmConnection, self).test_connect()
        pm.parent("leftShoulder_GRP", "chest_CON", "root_transform_CON")

        self.controls = \
            ["leftShoulder_attach_GRP", "body_CON", "root_transform_CON"]

        for i in range(3):
            try:
                self.controls[i] = pm.PyNode(self.controls[i])
            except:
                self.controls[i] = pm.spaceLocator(n=self.controls[i])

        pm.move(self.controls[1], [0.0, 91.23, -0.45], a=1)

        root_con = self.controls[-1]
        pm.parent("body_CON", root_con)
        pm.parent("chest_CON", "body_CON")

        pm.select(cl=1)

        root = pm.joint(p=[17.19, 138.49, 0.94], a=1)
        pm.joint(p=[40.69, 138.49, 1.44], a=1)
        pm.joint(p=[68.17, 138.49, 2.02], a=1)
        pm.joint(p=[75.66, 138.49, 2.18], a=1)

        root_con = self.controls[-1]

        self.arm = Rig(root, side="left", root_control=root_con)

    # @unittest.skip("")
    def test_connect(self):
        arm = self.arm
        arm.twist()
        arm.ikfk_switch()
        arm.fk()
        arm.ik()

        controls = self.controls
        # ["leftShoulder_attach_GRP", "body_CON", "root_transform_CON"]
        spaces = arm.connect(controls)
        self.assertTrue(spaces,
                        "connection failed")

    @classmethod
    def tearDownClass(cls):
        try:
            from tools.control_shapes import ControlShapes
            json_file = __file__.split("tests")[0] + "/results/arm.json"
            cs = ControlShapes()
            cs.load(json_file=json_file)
        except:
            pass
        pm.saveAs("result.ma", type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == "__main__":
    from maya import standalone, cmds

    standalone.initialize(name='python')
    cmds.loadPlugin("lookdevKit")  # not necessary if $PYMEL_SKIP_INIT=0

    # unittest.main(verbosity=3, failfast=1)

    test_case = TestShoulderArmConnection
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    runner = unittest.TextTestRunner(verbosity=3, failfast=1).run(suite)
