"""
test for coloring shapes
"""

import unittest
import pymel.core as pm
from tools.color_shapes import ColorShapes


class ColorShapesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"
        cls.cs = ColorShapes()
        pm.newFile(f=1)

    def tearDown(self):
        pm.select(cl=1)

    def test_color_by_name(self):
        self.assertTrue(self.cs.name("red"),
                        "shape did not change red")
        return

    def test_color_by_type(self):
        self.assertTrue(self.cs.type("fk"),
                        "shape did not change fk blue")

    def test_color_by_rgb(self):
        self.assertTrue(self.cs.rgb([134, 23, 90]),
                        "shape did not turn rgb = [134, 23, 90]")

    def test_assign_by_name(self):
        self.assertTrue(self.cs.name("hashdash", rgb=[134, 173, 255], add=1),
                        "did not add hashdash")

    def test_assign_by_type(self):
        self.assertFalse(self.cs.type("ik", name="hashdash", add=1),
                         "hashdash assigned to ik")

    def test_assign_by_type_name(self):
        self.assertTrue(self.cs.type("ik", name="peachpuff", add=1),
                        "did not assign yellow to ik")

    @classmethod
    def tearDownClass(cls):
        pm.saveAs("result.ma", type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == '__main__':
    from maya import standalone

    standalone.initialize(name='python')
    unittest.main(verbosity=2, failfast=1)
