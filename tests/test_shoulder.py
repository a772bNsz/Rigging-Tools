import unittest
import pymel.core as pm
from tools.shoulder import Rig


class TestShoulder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"

    def setUp(self):
        pm.newFile(f=1)

        root = pm.joint(p=[8.91, 142.2, 0.97])
        pm.joint(p=[17.19, 138.49, 0.93])

        root_con = pm.spaceLocator(n="root_transform_CON")

        self.shoulder = Rig(root, side="left", root_control=root_con)

    @unittest.skip("")
    def test_stretch_ik(self):
        shoulder = self.shoulder

        name = "Shoulder"
        start = shoulder.result_chain["root"]
        end = shoulder.result_chain["end"]

        # IK single chain handle
        handle, effector = pm.ikHandle(n=name + "_HDL",
                                       sj=start,
                                       ee=end,
                                       sol="ikSCSolver")
        effector.rename(name + "_EFF")

        side = shoulder.side
        locator = pm.spaceLocator(n=side + name + "_LOC")
        pm.matchTransform(locator, end, pos=1)

        pm.parent(handle, locator)
        pm.hide(locator)

        shoulder.stretch_ik(name, start, end, handle)
        self.assertTrue(shoulder.stretch_ik_nodes,
                        "stretch IK failed")

    @unittest.skip("")
    def test_ik(self):
        shoulder = self.shoulder

        shoulder.ik()
        self.assertTrue(shoulder.ik_nodes,
                        "shoulder IK failed")

    @unittest.skipIf(__name__ == "__main__", "")
    def test_connect(self):
        control = pm.spaceLocator(n="chest_CON")
        control.t.set(0.0, 139.22, 0.7)

        shoulder = self.shoulder
        shoulder.ik()
        shoulder.connect(control=control)
        self.assertTrue(shoulder.connect_nodes,
                        "connection failed")

    @unittest.skipIf(__name__ == "__main__", "")
    def test_right(self):
        left_root = self.shoulder.result_chain["root"]
        root = pm.mirrorJoint(left_root, mirrorYZ=1, mirrorBehavior=1)[0]
        pm.parent(root, w=1)
        root = pm.PyNode(root)

        root_con = pm.PyNode("root_transform_CON")
        control = pm.spaceLocator(n="chest_CON")
        control.t.set(0.0, 139.22, 0.7)

        shoulder = Rig(root, side="right", root_control=root_con)
        shoulder.ik()
        shoulder.connect(control=control)
        self.assertTrue(shoulder.connect_nodes, "connection failed")

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


class TestLeftRightShoulders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"

    def setUp(self):
        pm.newFile(f=1)

        root_con = pm.spaceLocator(n="root_transform_CON")
        chest_con = pm.spaceLocator(n="chest_CON")
        chest_con.t.set(0.0, 139.22, 0.7)
        chest_con.setParent(root_con)
        self.controls = chest_con

        left_root = pm.joint(p=[8.91, 142.2, 0.97])
        pm.joint(p=[17.19, 138.49, 0.93])

        self.left_shoulder = Rig(left_root, side="left", root_control=root_con)

        right_root = pm.PyNode(
            pm.mirrorJoint(left_root, mirrorYZ=1, mirrorBehavior=1)[0])
        pm.parent(right_root, w=1)

        self.right_shoulder = \
            Rig(right_root, side="right", root_control=root_con)

    def test_both_shoulders(self):
        for side in ["left", "right"]:
            shoulder = getattr(self, side + "_shoulder")
            shoulder.ik()
            shoulder.connect(control=self.controls)
        self.assertTrue(shoulder.connect_nodes,
                        "connection failed")

    @classmethod
    def tearDownClass(cls):
        try:
            from tools.control_shapes import ControlShapes
            json_file = __file__.split("tests")[0] + "/results/arms.json"
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

    test_case = TestLeftRightShoulders
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    runner = unittest.TextTestRunner(verbosity=3, failfast=1).run(suite)
