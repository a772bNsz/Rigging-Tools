import unittest
import pymel.core as pm
from tools.spine import Rig


class TestSpine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"
        cls.spine = Rig()
        pm.newFile(f=1)

    def setUp(self):
        pm.newFile(f=1)
        self.spine.root_joint = \
            pm.joint(n="spine1_result_JNT", p=[0.0, 91.23, -0.45])
        pm.joint(n="spine2_result_JNT", p=[0.0, 99.23, -0.37])
        pm.joint(n="spine3_result_JNT", p=[0.0, 107.23, -0.19])
        pm.joint(n="spine4_result_JNT", p=[0.0, 115.23, 0.05])
        pm.joint(n="spine5_result_JNT", p=[0.0, 123.23, 0.3])
        pm.joint(n="spine6_result_JNT", p=[0.0, 131.22, 0.53])
        pm.joint(n="spine7_result_JNT", p=[0.0, 139.22, 0.7])

    @unittest.skip("")
    def test_ik_spline(self):
        self.assertTrue(self.spine.ik_spline(),
                        "spline handle/curve not in Outliner")

    @unittest.skip("")
    def test_setup_controls(self):
        self.spine.ik_spline()
        self.assertTrue(self.spine.setup_controls(),
                        "not all setup controls are made")

    @unittest.skip("")
    def test_advanced_twist(self):
        self.spine.ik_spline()
        self.spine.setup_controls()
        self.assertTrue(self.spine._advanced_twist(),
                        "bind joints or spline twist settings erred")

    @unittest.skip("")
    def test_squash_stretch(self):
        self.spine.ik_spline()
        self.spine.setup_controls()
        self.spine._advanced_twist()
        self.assertIsNone(self.spine._squash_stretch(),
                          "math nodes for squash and stretch erred")

    def test_connect(self):
        self.spine.ik_spline()
        self.spine.setup_controls()
        self.spine._advanced_twist()
        self.spine._squash_stretch()
        self.assertIsNone(self.spine.connect("body_CON"),
                          "did not connect spine")

    def test_clean_up(self):
        self.spine.ik_spline()
        self.spine.setup_controls()
        self.spine.guts()
        self.assertIsNone(self.spine.clean_up(), "clean up failed")

    @classmethod
    def tearDownClass(cls):
        pm.saveAs("result.ma", type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == '__main__':
    from maya import standalone, cmds

    standalone.initialize(name='python')
    cmds.loadPlugin("lookdevKit")

    unittest.main(verbosity=2, failfast=1)
