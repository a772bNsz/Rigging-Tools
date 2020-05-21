"""
test for coloring shapes
"""

import unittest
import pymel.core as pm
from pymel.util.path import path
from tools.color_shapes import ColorShapes
from tools.control_shapes import ControlShapes
import json


class ColorShapesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"
        pm.newFile(f=1)
        cls.shapes = ControlShapes()
        cls.cs = ColorShapes()

        # ~/Rigging-Tools/results/color_shapes.json
        f = path(__file__).name.split(".")[0] + ".json"
        d = path(__file__).dirname().replace("tests", "results")
        cls.json_file = path(d + "/" + f)
        with open(cls.cs.json_file, "w") as f:
            dictionary = {"yellow": [255, 255, 0]}
            json.dump(dictionary, f, indent=4)

        cls.cs.get = cls.cs._get()

    def setUp(self):
        self.cs.sel = [self.shapes.gear()]

    def tearDown(self):
        pm.select(cl=1)

    def test_assign(self):
        self.cs._assign("ik", rgb=self.cs.get["yellow"])
        self.assertEqual(self.cs.get["ik"], self.cs.get["yellow"],
                         "did not assign")

    def test_set_by_name(self):
        with self.assertRaises(ValueError):
            self.cs.set("fk")

    def test_set_by_rgb(self):
        self.cs.sel[0].rename("fuchsia")
        self.assertTrue(self.cs.set([255, 0, 255]), "did not set by rgb")

    def test_set_update_by_name(self):
        self.cs.sel[0].rename("aqua")
        self.cs.set("aqua", rgb=[0, 255, 255], add=1)
        self.assertTrue(self.cs.set("fk", name="aqua", add=1),
                        "did not assign by name")

    def test_set_update_by_rgb(self):
        self.cs.sel[0].rename("yellow")
        self.assertTrue(self.cs.set("left", rgb=[255, 255, 0], add=1),
                        "did not assign by rgb")

    @classmethod
    def tearDownClass(cls):
        f = path(__file__).name.split(".")[0] + ".ma"
        pm.saveAs(f, type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == '__main__':
    from maya import standalone

    standalone.initialize(name='python')
    unittest.main(verbosity=2, failfast=1)
