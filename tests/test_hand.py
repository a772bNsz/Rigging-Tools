import unittest
import pymel.core as pm
from tools.hand import Rig
from tests.test_arm import TestArm


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
        pm.joint(p=[73.27, 136.91, 6.71])
        pm.joint(p=[74.76, 136.39, 7.78])
        pm.joint(p=[76.83, 135.66, 9.28])

        root_con = pm.spaceLocator(n="root_transform_CON")
        self.hand = Rig(root, side="left", root_control=root_con)

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

        aim_loc = pm.spaceLocator(n="aim_LOC")
        up_loc = pm.spaceLocator(n="up_LOC")
        up_loc.ty.set(3)
        up_loc.setParent(aim_loc)

        thumb_finger = self.hand.result_chain["thumb"].values()
        thumb_end = thumb_finger[-1]
        pm.matchTransform(aim_loc, thumb_end)

        thumb_start = thumb_finger[0]
        aim_const = pm.aimConstraint(aim_loc, thumb_start,
                                     mo=1,
                                     aimVector=[1, 0, 0],
                                     upVector=[0, 1, 0],
                                     worldUpType="objectRotation",
                                     worldUpVector=[0, 1, 0],
                                     worldUpObject=up_loc)

        aim_loc.rx.set(aim_loc.rx.get() + 90)

        aim_setup = aim_const.target.inputs()
        pm.delete(aim_setup)
        pm.makeIdentity(thumb, apply=1, r=1)

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

        # pinky
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

    def test_connect(self):
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


class TestArmHandConnection(TestArm):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"

    def setUp(self):
        pm.newFile(f=1)
        super(TestArmHandConnection, self).setUp()
        super(TestArmHandConnection, self).test_connect()

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
        pm.joint(p=[73.27, 136.91, 6.71])
        pm.joint(p=[74.76, 136.39, 7.78])
        pm.joint(p=[76.83, 135.66, 9.28])

        root_con = pm.PyNode("root_transform_CON")
        self.hand = Rig(root, side="left", root_control=root_con)

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

        aim_loc = pm.spaceLocator(n="aim_LOC")
        up_loc = pm.spaceLocator(n="up_LOC")
        up_loc.ty.set(3)
        up_loc.setParent(aim_loc)

        thumb_finger = self.hand.result_chain["thumb"].values()
        thumb_end = thumb_finger[-1]
        pm.matchTransform(aim_loc, thumb_end)

        aim_const = pm.aimConstraint(aim_loc, thumb,
                                     mo=1,
                                     aimVector=[1, 0, 0],
                                     upVector=[0, 1, 0],
                                     worldUpType="objectRotation",
                                     worldUpVector=[0, 1, 0],
                                     worldUpObject=up_loc)

        aim_loc.rx.set(aim_loc.rx.get() + 90)
        pm.delete(aim_const)
        pm.makeIdentity(thumb, apply=1, r=1)
        pm.delete(up_loc, aim_loc)

    # @unittest.skip("")
    def test_connect(self):
        hand = self.hand

        names = ["thumb", "index", "middle", "ring", "pinky"]
        fingers = hand.finger_attributes(fingers=names)

        params = {
            "palm": self.palm,
            "fingers": names
        }
        palm = hand.palm_attributes(**params)

        params = {
            "control": self.arm.result_chain["hand"],
            "bind_joint": self.arm.twist_nodes["lower"]["end_bind"],
            "settings": self.arm.controls["arm_settings"],
        }
        connected = hand.connect(**params)

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


if __name__ == "__main__":
    from maya import standalone, cmds

    standalone.initialize(name='python')
    cmds.loadPlugin("lookdevKit")  # not necessary if $PYMEL_SKIP_INIT=0

    # unittest.main(verbosity=3, failfast=1)

    test_case = TestArmHandConnection
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    runner = unittest.TextTestRunner(verbosity=3, failfast=1).run(suite)
