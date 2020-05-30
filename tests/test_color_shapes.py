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
        f = path(__file__).basename().split(".")[0] + ".json"
        d = path(__file__).dirname().replace("tests", "results")
        cls.cs.json_file = path(d + "/" + f)
        with open(cls.cs.json_file, "w") as f:
            dictionary = {"yellow": [255, 255, 0]}
            json.dump(dictionary, f, indent=4)

        cls.cs.get = cls.cs._get()

    def setUp(self):
        self.cs.sel = [self.shapes.gear()]

    def tearDown(self):
        pm.select(cl=1)

    def test_color_by_index(self):
        self.cs.index = 4
        self.cs.by_index()

    @classmethod
    def tearDownClass(cls):
        f = path(__file__).name.split(".")[0] + ".ma"
        pm.saveAs(f, type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == '__main__':
    from maya import standalone

    standalone.initialize(name='python')
    unittest.main(verbosity=2, failfast=1)
