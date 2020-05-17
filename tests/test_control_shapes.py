"""
test for control shapes
"""

import unittest
import pymel.core as pm
from tools.control_shapes import ControlShapes


class ControlShapesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"
        cls.cs = ControlShapes()
        pm.newFile(f=1)

    def tearDown(self):
        pm.select(cl=1)

    def test_replace(self):
        sel = pm.polyTorus()[0]
        self.assertTrue(self.cs.circle_nose(),
                        "did not replace selection with shape")

    def test_cube_to_locator(self):
        sel = pm.spaceLocator()  # active selection
        sel.t.set([10, 10, 10])
        self.cs.circle_nose()
        pos = self.cs.shape.getTranslation(space="world")
        self.assertTrue(all(map(lambda x: x == 10, pos)),
                        "shape position is not correct in world space")

    def test_multi_shape(self):
        self.assertTrue(self.cs.gear(),
                        "did not make combination shape")

    @classmethod
    def tearDownClass(cls):
        pm.saveAs("result.ma", type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == '__main__':
    from maya import standalone

    standalone.initialize(name='python')
    unittest.main(verbosity=2, failfast=1)
