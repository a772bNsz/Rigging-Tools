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
        sel.s.set([5] * 3)
        pm.parent(sel, top_node)
        self.cs.teardrop(save=1)
        data2 = self.cs.data

        self.assertGreater(len(data2), len(data1),
                           "json did not save correctly")

    def test_save_all(self):
        shapes = [self.cs.axis_bold()]
        shapes += [self.cs.four_arrow_thin()]
        shapes += [self.cs.gear()]

        pm.group(shapes, n="test_save_all")
        e = 0
        for i in shapes:
            i.rename("CON_"+str(e))
            self.cs._save(i.shape.get(), i)
            i.tx.set(e*5)
            e += 1

        self.assertTrue(path(self.cs.json_file).exists(),
                        "json file was not created")

    def test_load(self):
        pm.polyPlane(n="test_load")[0].s.set([5] * 3)
        self.cs.triangle(save=1)
        pm.delete("test_load")

        json_file = self.cs.json_file
        cs = ControlShapes()
        pm.polyPlane(n="test_load")

        self.assertTrue(cs._load(json_file=json_file, control="test_load"),
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
