import unittest
import pymel.core as pm
from pymel.util.path import path
from tools.head_neck import Rig
from tools.joint_chain import joint_chain


class HeadNeckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pm.newFile()

        # SPINE
        crv = pm.curve(
            d=3, periodic=0,
            knot=[0.0, 0.0, 0.0, 48.008, 48.008, 48.008],
            point=[[0.0, 91.23, -0.453], [0.0, 107.232, -0.272],
                   [0.0, 123.224, 0.35], [0.0, 139.223, 0.699]]
        )
        root = joint_chain(crv, number=7, name="spine#_result_JNT")
        crv.hide()

        pm.select(cl=1)
        from tools import ik_spline
        reload(ik_spline)
        spine = ik_spline.Rig(root)
        spine.ik_spline()
        spine.setup_controls()
        spine.guts()
        spine.connect("body_CON")
        spine.clean_up()

        from tools import control_shapes
        reload(control_shapes)
        cs = control_shapes.ControlShapes()
        f = path(__file__).dirname().replace("tests", "results")
        json_file = path(f + "/demo.json")
        cs.load(json_file=json_file)

        # NECK
        crv = pm.curve(
            d=3, periodic=0,
            knot=[0.0, 0.0, 0.0, 13.853, 13.853, 13.853],
            point=[[0.0, 145.635, 1.514], [0.0, 150.001, 3.037],
                   [0.0, 154.213, 4.916], [0.0, 158.525, 6.581]]
        )
        root = joint_chain(crv, number=4)

        cls.neck = Rig(root)

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

    @unittest.skip("")
    def test_connect(self):
        self.neck.ik_spline()
        self.neck.setup_controls()
        self.neck.guts()
        self.assertTrue(self.neck.connect("chest_CON"),
                        "did not connect neck to chest")

    @unittest.skip("")
    def test_space_switch(self):
        self.neck.ik_spline()
        self.neck.setup_controls()
        self.neck.guts()
        self.neck.connect("chest_CON")

        controls = ["neck_CON", "chest_CON", "body_CON", "root_transform_CON"]
        self.assertTrue(self.neck.space_switch(controls),
                        "did not apply space switch to head")

    @unittest.skip("")
    def test_clean_up_without_space_switch(self):
        self.neck.ik_spline()
        self.neck.setup_controls()
        self.neck.guts()
        self.assertTrue(self.neck.clean_up(),
                        "did not clean up")

    @unittest.skip("")
    def test_clean_up_with_space_switch(self):
        self.neck.ik_spline()
        self.neck.setup_controls()
        self.neck.guts()
        self.neck.connect("chest_CON")

        controls = ["neck_CON", "chest_CON", "body_CON", "root_transform_CON"]
        self.neck.space_switch(controls)
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
