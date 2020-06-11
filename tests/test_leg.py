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

        self.controls = ["hip_CON", "body_CON", "root_transform_CON"]

        parent = None
        for c in self.controls[::-1]:
            loc = pm.spaceLocator(n=c)
            loc.setParent(parent)
            parent = loc

        pm.setAttr(self.controls[1]+".translate", [0.0, 139.22, 0.7])
        root_con = pm.PyNode(self.controls[-1])

        self.leg = Rig(root, side="left", root_control=root_con)

    @unittest.skip("")
    def test_joint_chains(self):
        leg = self.leg
        made_all_chains = leg.result_chain and leg.ik_chain and leg.fk_chain
        self.assertTrue(made_all_chains,
                        "did not make and rename result, ik, and fk chains")

    @unittest.skip("")
    def test_controls(self):
        leg = self.leg
        made_all_controls = leg.controls["leg_settings"] \
                            and leg.controls["foot_ik"] \
                            and leg.controls["shin_fk"]
        self.assertTrue(made_all_controls,
                        "did not make all controls for leg rig")

    @unittest.skip("")
    def test_ikfk_switch(self):
        leg = self.leg
        blend_nodes = leg.ikfk_switch()
        self.assertTrue(blend_nodes,
                        "did not create IK/FK switch")

    @unittest.skip("")
    def test_fk_leg(self):
        leg = self.leg
        fk_leg_controls = leg.fk_leg()
        self.assertTrue(fk_leg_controls["thigh"],
                        "did not create fk leg")

    def test_basic_ik_leg_pv(self):
        leg = self.leg
        ik_chain = leg.ik_chain
        self.assertTrue(leg._basic_ik_leg(ik_chain, knee_type="pv"),
                        "did not create basic IK leg with pv knee")

    def test_ik_leg_stretch_pv(self):
        leg = self.leg
        pv_chain = leg.ik_chain
        leg._basic_ik_leg(pv_chain, knee_type="pv")
        self.assertTrue(leg._ik_stretch(pv_chain, knee_type="pv"),
                        "no flip IK leg does not stretch")
    
    def test_pv_knee(self):
        leg = self.leg
        pv_chain = leg.ik_chain
        pv_hdl, pv_knee_loc = leg._basic_ik_leg(pv_chain, knee_type="pv")
        leg._ik_stretch(pv_chain, knee_type="pv")
        self.assertTrue(leg._pv_knee(pv_chain, pv_knee_loc),
                        "did not create pv knee on IK leg")

    def test_dual_knee(self):
        self.assertTrue(self.leg._dual_knee(),
                        "did not create dual knee")

    def test_dual_knee_switch(self):
        leg = self.leg
        leg.ikfk_switch()
        pv_chain, no_flip_chain = leg._dual_knee()
        self.assertTrue(leg._dual_knee_switch(pv_chain, no_flip_chain),
                        "did not create dual knee switch")
        
    def test_ik_leg_pv(self):
        leg = self.leg
        self.assertTrue(leg.ik_leg(),
                        "did not create pv IK leg")

    def test_ik_leg_no_flip(self):
        leg = self.leg
        self.assertTrue(leg.ik_leg(pv=0, no_flip=1),
                        "did not create no flip IK leg")

    def test_dual_ik_leg(self):
        leg = self.leg
        leg.ikfk_switch()
        self.assertTrue(leg.ik_leg(pv=1, no_flip=1),
                        "did not create dual IK leg")

    def test_create_groups(self):
        leg = self.leg
        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg(pv=1, no_flip=1)
        const_groups = leg.create_groups()
        self.assertTrue(const_groups,
                        "did not create groups")

    def test_space_switch(self):
        leg = self.leg
        controls = self.controls

        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg(pv=1, no_flip=1)
        leg.create_groups()
        self.assertTrue(leg.space_switch(controls),
                        "did not create space switch")

    def test_clean_up(self):
        leg = self.leg
        controls = self.controls

        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg(pv=1, no_flip=1)
        leg.create_groups()
        leg.space_switch(controls)
        self.assertTrue(leg.clean_up(),
                        "did not clean up leg rig")

    @classmethod
    def tearDownClass(cls):
        try:
            from tools.control_shapes import ControlShapes
            json_file = __file__.split("tests")[0] + "/results/leg.json"
            cs = ControlShapes()
            cs.load(json_file=json_file)
        except:
            pass
        pm.saveAs("result.ma", type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == "__main__":
    from maya import standalone, cmds

    standalone.initialize(name="python")
    cmds.loadPlugin("lookdevKit")

    unittest.main(verbosity=2, failfast=1)
