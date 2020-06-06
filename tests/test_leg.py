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
        self.leg.ikfk_switch()

        self.leg.ik_chain["thigh"].ry.set(45)
        ik_toe_position = \
            self.leg.ik_chain["toe"].getTranslation(space="world")
        self.leg.controls["leg_settings"].FK_IK_blend.set(1)
        result_toe_position = \
            self.leg.result_chain["toe"].getTranslation(space="world")

        self.assertEqual(ik_toe_position, result_toe_position,
                         "FK/IK Blend not working")

    @unittest.skip("")
    def test_fk_leg(self):
        self.leg.ikfk_switch()
        self.leg.fk_leg()

        controls = self.leg.controls
        fk_chain = self.leg.fk_chain
        result_chain = self.leg.result_chain

        controls["thigh_fk"].length.set(2)
        controls["shin_fk"].ry.set(35)
        controls["shin_fk"].length.set(1.75)

        fk_toe_position = fk_chain["toe"].getTranslation(space="world")
        result_toe_position = result_chain["toe"].getTranslation(space="world")

        self.assertEqual(fk_toe_position, result_toe_position,
                         "fk leg was not made")

    def test_ik_leg_without_dual_knee(self):
        leg = self.leg
        leg.ikfk_switch()
        self.leg.fk_leg()
        leg.controls["leg_settings"].FK_IK_blend.set(1)
        leg.ik_leg(dual_knee=0)

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
