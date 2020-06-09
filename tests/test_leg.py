import unittest
import pymel.core as pm
from tools.leg import Rig


class TestLeg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"

    def setUp(self):
        pm.newFile(f=1)

        root = pm.joint(p=[8.93, 83.9, 0.93])  # thigh
        pm.joint(p=[8.93, 53.22, 2.37])  # shin
        pm.joint(p=[8.93, 11.02, -3.94])  # foot
        pm.joint(p=[8.93, 2.27, 7.47])  # ball
        pm.joint(p=[8.93, 1.82, 19.65])  # toe

        self.leg = Rig(root, side="left")

    @unittest.skip("")
    def test_init_chain(self):
        self.assertTrue(str(self.leg.ik_chain["thigh"]) == "leftThigh_IK_JNT",
                        "IK thigh not correctly named")
        self.assertTrue(str(self.leg.fk_chain["toe"]) == "leftToe_FK_JNT",
                        "FK toe not correctly named")

    @unittest.skip("")
    def test_init_controls(self):
        position = self.leg.controls["knee_ik"].getTranslation(space="world")
        knee_position = round(position[2], 2) == 12.37
        self.assertTrue(knee_position,
                        "knee control not where expected")

    @unittest.skip("")
    def test_ikfk_switch(self):
        leg = self.leg
        blend_nodes = leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg()
        self.assertTrue(blend_nodes,
                        "did not create IK/FK switch")

    @unittest.skip("")
    def test_cleanup(self):
        leg = self.leg
        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg()
        self.assertTrue(leg.cleanup(),
                        "did not clean up")

    # @unittest.skip("")
    def test_space_switch(self):
        leg = self.leg
        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg()
        leg.cleanup()
        controls = ["hip_CON", "body_CON", "root_transform_CON"]
        for c in controls:
            c = pm.spaceLocator(n=c)
        self.assertTrue(leg.space_switch(controls),
                        "did not create space switch")

    @unittest.skip("")
    def test_fk_leg(self):
        leg = self.leg
        self.assertTrue(leg.fk_leg(),
                        "did not create fk leg")

    @unittest.skip("")
    def test_no_flip_knee(self):
        leg = self.leg
        self.assertTrue(leg._dual_knee("noFlip"),
                        "did not create no flip knee")

    @unittest.skip("")
    def test_pv_knee(self):
        leg = self.leg
        self.assertTrue(leg._dual_knee("pv"),
                        "did not create pole vector knee")

    @unittest.skip("")
    def test_dual_knee_switch(self):
        leg = self.leg
        no_flip_chain = leg._dual_knee("noFlip")
        pv_chain = leg._dual_knee("pv")
        self.assertTrue(leg._dual_knee_switch(no_flip_chain, pv_chain),
                        "did not create dual knee switch")

    @unittest.skip("")
    def test_ik_leg(self):
        leg = self.leg
        self.assertTrue(leg.ik_leg(), "ik leg was not made")

    @classmethod
    def tearDownClass(cls):
        from tools.control_shapes import ControlShapes
        json_file = __file__.split("tests")[0] + "/results/leg.json"
        cs = ControlShapes()
        cs.load(json_file=json_file)
        pm.saveAs("result.ma", type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == "__main__":
    from maya import standalone, cmds

    standalone.initialize(name="python")
    cmds.loadPlugin("lookdevKit")

    unittest.main(verbosity=2, failfast=1)
