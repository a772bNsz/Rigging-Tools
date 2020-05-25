"""
test for maya version
"""

import unittest
import pymel.core as pm
from pymel.util.path import path
from tools.head_neck import Rig


class HeadNeckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pm.newFile()
        d = path(__file__).dirname().replace("tests", "results")
        ma = path(d + "/head_neck_start.ma")
        pm.importFile(ma, type="mayaAscii", ignoreVersion=1, renameAll=1,
                      mergeNamespacesOnClash=0, namespace=":", options="v=0;",
                      preserveReferences=1, importTimeRange="combine")
        cls.neck = Rig()
        cls.neck.root_joint = pm.PyNode("neck_base_result_JNT")

    @unittest.skip("")
    def test_ik_spline(self):
        self.assertTrue(self.neck.ik_spline(),
                        "neck IK spline not made")

    @unittest.skip("")
    def test_setup_controls(self):
        self.neck.ik_spline()
        self.assertTrue(self.neck.setup_controls(),
                        "did not set up controls")

    @unittest.skip("")
    def test_advanced_twist(self):
        self.neck.ik_spline()
        self.neck.setup_controls()
        self.assertTrue(self.neck._advanced_twist(),
                        "did not set up advanced twist")

    @unittest.skip("")
    def test_squash_stretch(self):
        self.neck.ik_spline()
        self.neck.setup_controls()
        self.neck._advanced_twist()
        self.assertTrue(self.neck._squash_stretch(),
                        "did not set up squash and stretch")

    @unittest.skip("")
    def test_guts(self):
        self.neck.ik_spline()
        self.neck.setup_controls()
        self.assertTrue(self.neck.guts(),
                        "did not set up guts")

    def test_connect(self):
        self.neck.ik_spline()
        self.neck.setup_controls()
        self.neck.guts()
        self.assertTrue(self.neck.connect("chest_CON"),
                        "did not connect neck to chest")

    @unittest.skip("")
    def test_clean_up(self):
        self.neck.ik_spline()
        self.neck.setup_controls()
        self.neck.guts()
        self.assertTrue(self.neck.clean_up(),
                        "did not clean up")

    @classmethod
    def tearDownClass(cls):
        pm.system.saveAs("result.ma", type="mayaAscii")
        print "\n>>>>>", pm.system.sceneName()


if __name__ == '__main__':
    from maya import standalone, cmds

    standalone.initialize(name='python')
    cmds.loadPlugin("lookdevKit")  # not necessary if $PYMEL_SKIP_INIT=0
    unittest.main(verbosity=3, failfast=1)
