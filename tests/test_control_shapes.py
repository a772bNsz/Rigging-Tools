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

    @unittest.skip("")
    def test_default(self):
        name = "arrow_circle"
        shape = getattr(self.cs, name)()
        position = all(x == 0 for x in shape.t.get())
        self.assertTrue(position, "default shape not created")

    @unittest.skip("")
    def test_match_locator(self):
        selected = pm.spaceLocator(n="test_match_by_bbx")
        selected.ty.set(2)
        selected.r.set([1.67, 0, -45])
        selected.s.set([2.71]*3)

        bbx1 = map(lambda s: s[1] - s[0], zip(*selected.getBoundingBox()))
        name = "circle_spikes"
        shape = self.cs._match_locator(name, selected)
        bbx2 = map(lambda s: s[1] - s[0], zip(*shape.getBoundingBox()))
        within_original_bbx = max(bbx1) >= max(bbx2)
        self.assertTrue(within_original_bbx,
                        "new shape is larger than original shape")

    @unittest.skip("")
    def test_save(self):
        selected = pm.spaceLocator()
        selected.ty.set(2)
        selected.r.set([1.67, 0, -45])
        selected.s.set([2.71]*3)

        pm.duplicate(n="test_save")
        f = path(__file__).dirname().replace("tests", "results")
        json_file = path(f + "/test_save.json")
        controls = [self.cs.teardrop()]  # active selection on control
        self.assertTrue(self.cs.save(json_file=json_file, controls=controls),
                        "did not save")

    @unittest.skip("")
    def test_save_overwrite(self):
        f = path(__file__).dirname().replace("tests", "results")
        json_file = path(f + "/test_save_overwrite.json")

        sel = pm.polyCube(n="test_save_overwrite")[0]
        sel.s.set([10, 20, 5])
        controls = [self.cs.eight_star()]
        self.cs.save(json_file=json_file, controls=controls)

        pm.select(sel)
        sel.s.set([5] * 3)
        controls = [self.cs.gear()]
        self.cs.save(json_file=json_file, controls=controls)

        with open(json_file) as f:
            data = json.load(f)

        updated = data["test_save_overwrite"]["control"].count("curve")
        self.assertTrue(updated, "did not save")

    @unittest.skip("")
    def test_save_all(self):
        f = path(__file__).dirname().replace("tests", "results")
        json_file = path(f + "/test_save_all.json")

        controls = []; e = 1
        for shp in ["axis_bold", "four_arrow_thin", "gear"]:
            controls += [getattr(self.cs, shp)().rename("CON_"+str(e))]
            controls[-1].tx.set(e*5)
            controls[-1].ry.set(e*30)
            controls[-1].sz.set(e*1.2)
            pm.select(cl=1)
            e += 1

        self.cs.save(json_file=json_file, controls=controls)

        with open(json_file) as f:
            data = json.load(f)

        self.assertTrue(len(data) == 3, "json file was not created")

    @unittest.skipIf(
        not path("/root/workdir/results/test_save_all.json").exists(),
        "No such file or directory: test_save_all.json"
    )
    def test_load(self):
        controls = []
        for i in range(1, 4):
            controls += [pm.spaceLocator().rename("CON_"+str(i))]
            controls[-1].tx.set(i*5)
            controls[-1].ry.set(i*30)
            controls[-1].sz.set(i*1.2)
            pm.select(cl=1)

        f = path(__file__).dirname().replace("tests", "results")
        json_file = path(f + "/test_save_all.json")
        self.cs.load(json_file=json_file)

        locator = pm.attributeQuery("localScaleY", node="CON_3", ex=1)
        self.assertFalse(locator, "did not load shapes from file")

    @classmethod
    def tearDownClass(cls):
        pm.saveAs("result.ma", type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == '__main__':
    from maya import standalone

    standalone.initialize(name='python')
    unittest.main(verbosity=2, failfast=1)
