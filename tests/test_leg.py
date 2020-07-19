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

    @unittest.skip("")
    def test_basic_ik_leg_pv(self):
        leg = self.leg
        ik_chain = leg.ik_chain
        self.assertTrue(leg._basic_ik_leg(ik_chain, knee_type="pv"),
                        "did not create basic IK leg with pv knee")

    @unittest.skip("")
    def test_ik_leg_stretch_pv(self):
        leg = self.leg
        pv_chain = leg.ik_chain
        leg._basic_ik_leg(pv_chain, knee_type="pv")
        self.assertTrue(leg._ik_stretch(pv_chain, knee_type="pv"),
                        "no flip IK leg does not stretch")

    @unittest.skip("")
    def test_pv_knee(self):
        leg = self.leg
        pv_chain = leg.ik_chain
        pv_hdl, pv_knee_loc = leg._basic_ik_leg(pv_chain, knee_type="pv")
        leg._ik_stretch(pv_chain, knee_type="pv")
        self.assertTrue(leg._pv_knee(pv_chain, pv_knee_loc),
                        "did not create pv knee on IK leg")

    @unittest.skip("")
    def test_dual_knee(self):
        self.assertTrue(self.leg._dual_knee(),
                        "did not create dual knee")

    @unittest.skip("")
    def test_dual_knee_switch(self):
        leg = self.leg
        leg.ikfk_switch()
        pv_chain, no_flip_chain = leg._dual_knee()
        self.assertTrue(leg._dual_knee_switch(pv_chain, no_flip_chain),
                        "did not create dual knee switch")

    @unittest.skip("")
    def test_ik_leg_pv(self):
        leg = self.leg
        self.assertTrue(leg.ik_leg(),
                        "did not create pv IK leg")

    @unittest.skip("")
    def test_ik_leg_no_flip(self):
        leg = self.leg
        self.assertTrue(leg.ik_leg(pv=0, no_flip=1),
                        "did not create no flip IK leg")

    @unittest.skip("")
    def test_dual_ik_leg(self):
        leg = self.leg
        leg.ikfk_switch()
        self.assertTrue(leg.ik_leg(pv=1, no_flip=1),
                        "did not create dual IK leg")

    @unittest.skip("")
    def test_create_groups(self):
        leg = self.leg
        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg(pv=1, no_flip=1)
        const_groups = leg.create_groups()
        self.assertTrue(const_groups,
                        "did not create groups")

    @unittest.skip("")
    def test_space_switch(self):
        leg = self.leg
        controls = self.controls

        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg(pv=1, no_flip=1)
        leg.create_groups()
        self.assertTrue(leg.space_switch(controls),
                        "did not create space switch")

    # @unittest.skip("")
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


class TestFoot(unittest.TestCase):
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

        controls = ["hip_CON", "body_CON", "root_transform_CON"]

        parent = None
        for c in controls[::-1]:
            loc = pm.spaceLocator(n=c)
            loc.setParent(parent)
            parent = loc

        pm.setAttr(controls[1]+".translate", [0.0, 139.22, 0.7])
        root_con = pm.PyNode(controls[-1])

        leg = Rig(root, side="left", root_control=root_con)
        leg.ikfk_switch()
        leg.fk_leg()
        leg.ik_leg(pv=1, no_flip=1)
        leg.create_groups()
        leg.space_switch(controls)
        leg.clean_up()

        self.leg = leg
        self.foot = leg.foot

        locators = self.foot.ik_foot_setup()

        locators["heel"].t.set(9.42, -0.16, -10.07)
        locators["outer"].t.set(15.11, 0.0, 13.66)
        locators["inner"].t.set(3.34, 0.0, 11.72)
        locators["toe"].t.set(8.93, 1.82, 19.65)
        locators["ball"].t.set(8.93, 2.27, 7.47)

    @unittest.skip("")
    def test_cleanup(self):
        foot = self.foot
        self.assertTrue(foot._clean_up(), "clean up failed")

    @unittest.skip("")
    def test_roll(self):
        foot = self.foot
        added_feature = foot._roll()
        self.assertTrue(added_feature, "roll feature failed")

    @unittest.skip("")
    def test_tilt(self):
        foot = self.foot
        added_feature = foot._tilt()
        self.assertTrue(added_feature,  "tilt feature failed")

    @unittest.skip("")
    def test_lean(self):
        foot = self.foot
        added_feature = foot._lean()
        self.assertTrue(added_feature, "lean feature failed")

    @unittest.skip("")
    def test_toe_spin(self):
        foot = self.foot
        added_feature = foot._toe_spin()
        self.assertTrue(added_feature, "toe spin feature failed")

    @unittest.skip("")
    def test_toe_wiggle(self):
        foot = self.foot
        added_feature = foot._toe_wiggle()
        self.assertTrue(added_feature, "toe wiggle feature failed")

    # @unittest.skip("")
    def test_ik_foot(self):
        foot = self.foot
        created_smart_foot_control = foot.ik_foot()  # returns True
        self.assertTrue(created_smart_foot_control,
                        "did not create smart foot control")

    def tearDown(self):
        leg_settings = self.leg.controls["leg_settings"]
        leg_settings.FK_IK_blend.set(1)

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


class TestBothLegs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"

    def setUp(self):
        pm.newFile(f=1)

        self.controls = ["hip_CON", "body_CON", "root_transform_CON"]

        parent = None
        for c in self.controls[::-1]:
            loc = pm.spaceLocator(n=c)
            loc.setParent(parent)
            parent = loc

        pm.setAttr(self.controls[1]+".translate", [0.0, 91.23, -0.45])
        root_con = pm.PyNode(self.controls[-1])

        pm.select(cl=1)
        root = pm.joint(p=[8.93, 83.9, 0.93])  # thigh
        pm.joint(p=[8.93, 53.22, 2.37])  # shin
        pm.joint(p=[8.93, 11.02, -3.94])  # foot
        pm.joint(p=[8.93, 2.27, 7.47])  # ball
        pm.joint(p=[8.93, 1.82, 19.65])  # toe

        self.left_leg = Rig(root, side="left", root_control=root_con)

        pm.select(cl=1)
        root = pm.duplicate(root)[0]
        root.tx.set(root.tx.get() * -1)
        # root = pm.PyNode(
        #     pm.mirrorJoint(root, mirrorYZ=1, mirrorBehavior=1)[0])
        # pm.parent(root, w=1)

        self.right_leg = Rig(root, side="right", root_control=root_con)

    @unittest.skip("")
    def test_init(self):
        right_leg = self.right_leg.result_chain
        left_leg = self.left_leg.result_chain
        self.assertTrue(right_leg and left_leg,
                        "did not initialize left and right legs")

    @unittest.skip("")
    def test_legs(self):
        controls = self.controls  # hip, body, root

        rigged_legs = []
        for side in ["left", "right"]:
            leg = getattr(self, side + "_leg")
        
            leg.ikfk_switch()
            leg.fk_leg()
            leg.ik_leg(pv=1, no_flip=1)
            leg.create_groups()
            leg.space_switch(controls)
            rigged = leg.clean_up()  # returns True
            rigged_legs += [rigged]

        self.assertTrue(all(rigged_legs),
                        "did not rig legs")

    # @unittest.skip("")
    def test_legs_and_feet(self):
        controls = self.controls  # hip, body, root

        for side in ["left", "right"]:
            leg = getattr(self, side + "_leg")

            leg.ikfk_switch()
            leg.fk_leg()
            leg.ik_leg(pv=1, no_flip=1)
            leg.create_groups()
            leg.space_switch(controls)
            leg.clean_up()  # returns True

        self.left_leg.ik_foot_setup()
        locators = self.left_leg.locators
        locators["heel"].t.set(9.42, -0.16, -10.07)
        locators["outer"].t.set(15.11, 0.0, 13.66)
        locators["inner"].t.set(3.34, 0.0, 11.72)
        locators["toe"].t.set(8.93, 1.82, 19.65)
        locators["ball"].t.set(8.93, 2.27, 7.47)
        rigged_left_foot = self.left_leg.ik_foot()

        self.right_leg.ik_foot_setup()
        locators = self.right_leg.locators
        locators["heel"].t.set(-9.42, -0.16, -10.07)
        locators["outer"].t.set(-15.11, 0.0, 13.66)
        locators["inner"].t.set(-3.34, 0.0, 11.72)
        locators["toe"].t.set(-8.93, 1.82, 19.65)
        locators["ball"].t.set(-8.93, 2.27, 7.47)
        rigged_right_foot = self.right_leg.ik_foot()

        self.assertTrue(all([rigged_left_foot, rigged_right_foot]),
                        "did not rig legs and feet")

    def tearDown(self):
        for side in ["left", "right"]:
            leg_settings = \
                getattr(self, side + "_leg").controls["leg_settings"]
            leg_settings.FK_IK_blend.set(1)

    @classmethod
    def tearDownClass(cls):
        try:
            from tools.control_shapes import ControlShapes
            json_file = __file__.split("tests")[0] + "/results/demo.json"
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

    # unittest.main(verbosity=2, failfast=1)

    test_case = TestBothLegs
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner(verbosity=2, failfast=1).run(suite)
