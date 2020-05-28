"""
test for control shapes
"""

import unittest
import pymel.core as pm
from pymel.util.path import path
from tools.control_shapes import ControlShapes
import json


class ControlShapesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"
        cls.cs = ControlShapes()

    def setUp(self):
        pm.newFile(f=1)

    def tearDown(self):
        pm.select(cl=1)

    def test_replace(self):
        pm.polyTorus()[0]
        self.assertTrue(self.cs.circle_nose(),
                        "did not replace selection with shape")

    def test_cube_to_locator(self):
        sel = pm.spaceLocator()  # active selection
        sel.t.set([10] * 3)
        pos = self.cs.circle_nose().getTranslation(space="world")
        self.assertTrue(all(map(lambda x: x == 10, pos)),
                        "shape position is not correct in world space")

    def test_multi_shape(self):
        self.assertTrue(self.cs.gear(),
                        "did not make combination shape")

    def test_save(self):
        pm.polyCylinder()[0].s.set([5] * 3)
        pm.duplicate(n="test_save")
        f = path(__file__).dirname().replace("tests", "results")
        json_file = path(f + "/test_save.json")
        controls = [self.cs.teardrop()]  # active selection on control
        self.assertTrue(self.cs.save(json_file=json_file, controls=controls),
                        "did not save")

    def test_save_overwrite(self):
        f = path(__file__).dirname().replace("tests", "results")
        json_file = path(f + "/test_save_overwrite.json")

        sel = pm.polyCube(n="test_save_overwrite")[0]
        sel.s.set([10, 20, 5])
        controls = [self.cs.eight_star()]
        self.cs.save(json_file=json_file, controls=controls)

        sel.s.set([5] * 3)
        controls = [self.cs.teardrop()]
        self.cs.save(json_file=json_file, controls=controls)

        with open(json_file) as f:
            data = json.load(f)

        self.assertEqual(data["test_save_overwrite"]["shape"], "teardrop",
                         "did not save")

    def test_save_all(self):
        f = path(__file__).dirname().replace("tests", "results")
        json_file = path(f + "/test_save_all.json")

        controls = []; e = 1
        for shp in ["axis_bold", "four_arrow_thin", "gear"]:
            method = getattr(self.cs, shp)
            controls += [method().rename("CON_"+str(e))]
            controls[-1].tx.set(e*5)
            pm.select(cl=1)
            e += 1

        self.cs.save(json_file=json_file, controls=controls)

        with open(json_file) as f:
            data = json.load(f)

        self.assertTrue(len(data) == 3, "json file was not created")

    @unittest.skip("")
    def test_load(self):
        pm.polyPlane(n="test_load")[0].s.set([5] * 3)
        self.cs.triangle(save=1)
        pm.delete("test_load")

        json_file = self.cs.json_file
        cs = ControlShapes()
        pm.polyPlane(n="test_load")

        self.assertTrue(cs.load(json_file=json_file, control="test_load"),
                        "did not load 'test_load'")

    @classmethod
    def tearDownClass(cls):
        f = path(__file__).name.split(".")[0] + ".ma"
        pm.saveAs(f, type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == '__main__':
    from maya import standalone

    standalone.initialize(name='python')
    unittest.main(verbosity=2, failfast=1)
