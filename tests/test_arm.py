import unittest
import pymel.core as pm
from tools.arm import Rig, Hand
from tests.test_shoulder import TestShoulder
from collections import OrderedDict


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


class TestHand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"

    def setUp(self):
        pm.newFile(f=1)

        # hand
        root = pm.joint(p=[68.17, 138.49, 2.02])

        pm.select(root)
        pinky = pm.joint(p=[72.26, 138.44, -0.63])
        pm.joint(p=[76.93, 138.44, -0.9])
        pm.joint(p=[79.19, 138.44, -0.9])
        pm.joint(p=[81.26, 138.44, -0.9])
        pm.joint(p=[83.04, 138.44, -0.9])

        pm.select(root)
        ring = pm.joint(p=[72.32, 138.85, 0.79])
        pm.joint(p=[77.23, 138.85, 0.67])
        pm.joint(p=[80.56, 138.85, 0.67])
        pm.joint(p=[83.09, 138.85, 0.67])
        pm.joint(p=[85.03, 138.85, 0.67])

        pm.select(root)
        middle = pm.joint(p=[72.32, 139.11, 2.14])
        pm.joint(p=[77.59, 139.11, 2.3])
        pm.joint(p=[81.01, 139.11, 2.3])
        pm.joint(p=[83.58, 139.11, 2.3])
        pm.joint(p=[85.66, 139.11, 2.3])

        pm.select(root)
        index = pm.joint(p=[72.23, 139.11, 3.62])
        pm.joint(p=[77.74, 139.11, 3.87])
        pm.joint(p=[80.85, 139.11, 3.87])
        pm.joint(p=[83.39, 139.11, 3.87])
        pm.joint(p=[85.33, 139.11, 3.87])

        pm.select(root)
        thumb = pm.joint(p=[71.11, 137.67, 5.15])
        pm.joint(p=[73.11, 137.19, 7.07])
        pm.joint(p=[74.7, 136.62, 7.9])
        pm.joint(p=[76.99, 136.14, 9.18])

        root_con = pm.spaceLocator(n="root_transform_CON")
        self.hand = Hand(root, side="left", root_control=root_con)

        fingers = {
            "thumb": thumb,
            "index": index,
            "middle": middle,
            "ring": ring,
            "pinky": pinky
        }

        for k, v in fingers.items():
            self.hand.finger_chain(v, name=k)

        middle = pm.spaceLocator(n="middle")
        middle.t.set([77.59, 139.11, 2.3])

        outer = pm.spaceLocator(n="outer")
        outer.t.set([75.37, 137.33, -1.16])

        inner = pm.spaceLocator(n="inner")
        inner.t.set([75.79, 137.55, 4.45])

        self.palm = [middle, inner, outer]

    @unittest.skip("")
    def test_finger_chain(self):
        # index
        root = pm.joint(p=[72.23, 139.11, 3.62])
        pm.joint(p=[77.74, 138.81, 3.87])
        pm.joint(p=[80.76, 138.09, 3.87])
        pm.joint(p=[83.1, 137.09, 3.87])
        pm.joint(p=[84.55, 135.82, 3.87])

        hand = self.hand
        name = "index"
        hand.finger_chain(root, name=name)
        self.assertTrue(hand.result_chain[name])

    @unittest.skip("")
    def test_all_finger_chains(self):
        hand = self.hand
        root = hand.result_chain["hand"]

        #pinky
        pm.select(root)
        pinky = pm.joint(p=[72.26, 138.44, -0.63])
        pm.joint(p=[76.93, 138.44, -0.9])
        pm.joint(p=[79.19, 138.44, -0.9])
        pm.joint(p=[81.26, 138.44, -0.9])
        pm.joint(p=[83.04, 138.44, -0.9])

        # ring
        pm.select(root)
        ring = pm.joint(p=[72.32, 138.85, 0.79])
        pm.joint(p=[77.23, 138.85, 0.67])
        pm.joint(p=[80.56, 138.85, 0.67])
        pm.joint(p=[83.09, 138.85, 0.67])
        pm.joint(p=[85.03, 138.85, 0.67])

        # middle
        pm.select(root)
        middle = pm.joint(p=[72.32, 139.11, 2.14])
        pm.joint(p=[77.59, 139.11, 2.3])
        pm.joint(p=[81.01, 139.11, 2.3])
        pm.joint(p=[83.58, 139.11, 2.3])
        pm.joint(p=[85.66, 139.11, 2.3])

        # index
        pm.select(root)
        index = pm.joint(p=[72.23, 139.11, 3.62])
        pm.joint(p=[77.74, 138.81, 3.87])
        pm.joint(p=[80.76, 138.09, 3.87])
        pm.joint(p=[83.1, 137.09, 3.87])
        pm.joint(p=[84.55, 135.82, 3.87])

        # thumb
        pm.select(root)
        thumb = pm.joint(p=[71.11, 137.67, 5.15])
        pm.joint(p=[73.11, 137.19, 7.07])
        pm.joint(p=[74.7, 136.62, 7.9])
        pm.joint(p=[76.99, 136.14, 9.18])

        fingers = {
            "thumb": thumb,
            "index": index,
            "middle": middle,
            "ring": ring,
            "pinky": pinky
        }

        for k, v in fingers.items():
            hand.finger_chain(v, name=k)
        self.assertEqual(len(hand.result_chain), 6,
                         "failed to make all five fingers")

    @unittest.skip("")
    def test_finger_controls(self):
        hand = self.hand
        name = "index"

        finger_chain = hand.result_chain[name]
        hand.finger_controls(finger_chain, name=name)

        finger_controls = hand.controls[name]
        self.assertTrue(finger_controls["base"]["sdk"] == "leftIndexBase_SDK",
                        "failed to make controls")

    @unittest.skip("")
    def test_all_finger_controls(self):
        hand = self.hand
        names = ["thumb", "index", "middle", "ring", "pinky"]

        for name in names:
            finger_chain = hand.result_chain[name]
            hand.finger_controls(finger_chain, name=name)

        self.assertTrue(hand.controls, "failed to make controls")

    @unittest.skip("")
    def test_finger_flop(self):
        hand = self.hand
        name = "index"

        finger_chain = hand.result_chain[name]
        finger_controls = hand.finger_controls(finger_chain, name=name)

        driver_con = finger_controls["1"]["con"]
        sdk_null = finger_controls["1"]["sdk"]

        flopped = hand.flop(driver_con, sdk_null)
        self.assertTrue(flopped, "flop failed")

    @unittest.skip("")
    def test_finger_curl(self):
        hand = self.hand
        name = "index"

        finger_chain = hand.result_chain[name]
        finger_controls = hand.finger_controls(finger_chain, name=name)
        curled = hand.curl(finger_controls)

        self.assertTrue(curled, "curl failed")
    
    @unittest.skip("")
    def test_finger_lean(self):
        hand = self.hand
        name = "index"

        finger_chain = hand.result_chain[name]
        finger_controls = hand.finger_controls(finger_chain, name=name)
        leaned = hand.lean(finger_controls)

        self.assertTrue(leaned, "lean failed")

    @unittest.skip("")
    def test_finger_spread(self):
        hand = self.hand
        name = "index"

        finger_chain = hand.result_chain[name]
        finger_controls = hand.finger_controls(finger_chain, name=name)
        spreaded = hand.spread(finger_controls)

        self.assertTrue(spreaded, "spread failed")

    @unittest.skip("")
    def test_all_finger_attributes(self):
        hand = self.hand
        names = ["index", "middle", "ring", "pinky"]

        for name in names:
            finger_chain = hand.result_chain[name]
            finger_controls = hand.finger_controls(finger_chain, name=name)

            driver_con = finger_controls["1"]["con"]
            sdk_null = finger_controls["1"]["sdk"]

            hand.flop(driver_con, sdk_null)

            sdk_nulls = [v["sdk"] for v in finger_controls.values()[2:]]
            hand.curl(driver_con, sdk_nulls)
            hand.spread(finger_controls)
            hand.lean(finger_controls)

        name = "thumb"
        finger_chain = hand.result_chain[name]
        finger_controls = hand.finger_controls(finger_chain, name=name)

        driver_con = finger_controls["1"]["con"]
        sdk_null = finger_controls["base"]["sdk"]
        hand.flop(driver_con, sdk_null, attr="ry")

        sdk_nulls = [v["sdk"] for v in finger_controls.values()[1:]]
        hand.curl(driver_con, sdk_nulls, attr="ry")

        self.assertTrue(hand.controls, "failed to make controls")

    @unittest.skip("")
    def test_finger_attributes(self):
        hand = self.hand

        names = ["index", "middle", "ring", "pinky"]
        done = hand.finger_attributes(fingers=names)
        self.assertTrue(done, "finger attributes failed")

    @unittest.skip("")
    def test_finger_length(self):
        hand = self.hand
        name = "index"

        finger_chain = hand.result_chain[name]
        finger_controls = hand.finger_controls(finger_chain, name=name)

        driver_con = finger_controls["1"]["con"]
        driven_objs = [v for v in finger_controls.values()[2:]]
        stretched = hand.length(driver_con, driven_objs)

        self.assertTrue(stretched, "stretch failed")

    @unittest.skip("")
    def test_palm_controls(self):
        hand = self.hand

        middle = pm.spaceLocator(n="middle")
        middle.t.set([77.59, 139.11, 2.3])

        outer = pm.spaceLocator(n="outer")
        outer.t.set([75.37, 137.33, -1.16])

        inner = pm.spaceLocator(n="inner")
        inner.t.set([75.79, 137.55, 4.45])

        hand_control = pm.spaceLocator(n="leftHand_CON")
        hand_control.t.set([72.23, 148.22, 3.62])

        params = {
            "hand_control": hand_control,
            "palm": [middle, inner, outer],
            "fingers": ["thumb", "index", "middle", "ring", "pinky"]
        }
        palmed = hand.palm_attributes(**params)
        self.assertTrue(palmed, "palm attributes failed")

    @unittest.skip("")
    def test_hand_controls(self):
        hand = self.hand

        names = ["index", "middle", "ring", "pinky"]
        fingers = hand.finger_attributes(fingers=names)

        params = {
            "palm": self.palm,
            "fingers": names
        }
        palm = hand.palm_attributes(**params)

        self.assertEqual(fingers, palm, "hand controls failed")

    def test_connection(self):
        hand = self.hand

        names = ["index", "middle", "ring", "pinky"]
        fingers = hand.finger_attributes(fingers=names)

        params = {
            "palm": self.palm,
            "fingers": names
        }
        palm = hand.palm_attributes(**params)

        connected = hand.connect()

        self.assertTrue(connected, "connection failed")

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


class TestBothArms(TestArm):
    @classmethod
    def setUpClass(cls):
        super(TestBothArms, cls).setUpClass()
        print ">>>>> SETUP"

    @classmethod
    def tearDownClass(cls):
        super(TestBothArms, cls).tearDownClass()
        print ">>>>> TEARDOWN"


if __name__ == "__main__":
    from maya import standalone, cmds

    standalone.initialize(name='python')
    cmds.loadPlugin("lookdevKit")  # not necessary if $PYMEL_SKIP_INIT=0

    # unittest.main(verbosity=3, failfast=1)

    test_case = TestHand
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    runner = unittest.TextTestRunner(verbosity=3, failfast=1).run(suite)
