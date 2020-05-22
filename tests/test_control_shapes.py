"""
test for control shapes
"""

import unittest
import pymel.core as pm
from pymel.util.path import path
from tools.control_shapes import ControlShapes


class ControlShapesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"
        cls.cs = ControlShapes()
        pm.newFile(f=1)

        d = path(__file__).dirname().replace("tests", "results")
        files = path(d).files("test_*.json")
        [f.remove_p() for f in files]

    def tearDown(self):
        pm.select(cl=1)

    def test_replace(self):
        pm.polyTorus()[0]
        self.assertTrue(self.cs.circle_nose(),
                        "did not replace selection with shape")

    def test_cube_to_locator(self):
        sel = pm.spaceLocator()  # active selection
        sel.t.set([10]*3)
        self.cs.circle_nose()
        pos = self.cs.shape.getTranslation(space="world")
        self.assertTrue(all(map(lambda x: x == 10, pos)),
                        "shape position is not correct in world space")

    def test_multi_shape(self):
        self.assertTrue(self.cs.gear(),
                        "did not make combination shape")

    def test_save(self):
        pm.polyCylinder()[0].s.set([5]*3)
        pm.duplicate(n="test_save")
        self.assertTrue(self.cs.teardrop(save=1),
                        "did not save")

    def test_save_overwrite(self):
        top_node = pm.group(n="test_save_overwrite")

        sel = pm.polyCube()[0]
        sel.s.set([10, 20, 5])
        pm.parent(sel, top_node)
        self.cs.eight_star(save=1)
        data1 = self.cs.data

        sel = pm.polyCylinder()[0]
        sel.s.set([5]*3)
        pm.parent(sel, top_node)
        self.cs.teardrop(save=1)
        data2 = self.cs.data

        self.assertGreater(len(data2), len(data1),
                           "json did not save correctly")

    @classmethod
    def tearDownClass(cls):
        f = path(__file__).name.split(".")[0] + ".ma"
        pm.saveAs(f, type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == '__main__':
    from maya import standalone

    standalone.initialize(name='python')
    unittest.main(verbosity=2, failfast=1)
