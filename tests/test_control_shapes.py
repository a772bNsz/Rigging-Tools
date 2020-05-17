"""
test for maya version
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

    def test_replace(self):
        replace = pm.polyTorus()[0]  # active selection
        shp = self.cs.cube()
        self.assertTrue(self.cs._replace(),
                        "did not replace selection with shape")

    def test_locator_to_cube(self):
        replace = pm.spaceLocator(p=[10, 10, 10])  # active selection
        shp = self.cs.cube()
        self.cs._replace()
        pos = shp.getTranslation(space="world")
        self.assertEqual(pos, [10, 10, 10],
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
