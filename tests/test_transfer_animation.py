import unittest
import pymel.core as pm
from os import path

from tools.transfer_animation import TransferAnimation


class TestTransferAnimation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.TransferAnimation = TransferAnimation()
        return

    def setUp(self):
        pm.newFile(f=1)

        self.src, = pm.polyCone(n="src",
                                r=1, h=2, sx=4, sy=1, sz=0, ax=(0, 1, 0), ch=0)
        self.trg, = pm.polyCone(n="trg",
                                r=0.5, h=5, sx=12, sy=1, sz=0, ax=(0, 1, 0),
                                ch=0)
        self.trg_offset, = pm.polyCone(n="trg_offset",
                                       r=3, h=5, sx=12, sy=1, sz=0,
                                       ax=(0, 1, 0), ch=0)

        root_dir = __file__.split("tests")[0]
        load_filename = path.join(root_dir, "results", "src.json")
        pm.select(self.src)
        self.TransferAnimation.load_data(load_filename, start_frame=None)
        return

    def test_default_load(self):
        root_dir = __file__.split("tests")[0]
        load_filename = path.join(root_dir, "results", "src.json")
        pm.select(self.trg)
        self.TransferAnimation.load_data(load_filename, start_frame=None)

        target_rotate_z = pm.keyframe(self.trg.rz, q=1, index=[0, 2], vc=1)
        source_rotate_z = pm.keyframe(self.src.rz, q=1, index=[0, 2], vc=1)

        self.assertEqual(target_rotate_z, source_rotate_z,
                         "animation curve doesn't match")

    def test_offset_load(self):
        root_dir = __file__.split("tests")[0]
        load_filename = path.join(root_dir, "results", "src.json")
        pm.select(self.trg_offset)
        self.TransferAnimation.load_data(load_filename, start_frame=30)

        trg_tc, trg_vc = \
            pm.keyframe(self.trg_offset.rz, q=1, tc=1), \
            pm.keyframe(self.trg_offset.rz, q=1, vc=1)
        src_tc, src_vc = \
            pm.keyframe(self.src.rz, q=1, tc=1), \
            pm.keyframe(self.src.rz, q=1, vc=1)

        different_keyframes = trg_tc != src_tc
        same_values = src_vc == trg_vc

        self.assertEqual(different_keyframes, same_values,
                         "animation curve doesn't match")

    # def tearDown(self):
    #     return

    @classmethod
    def tearDownClass(cls):
        pm.saveAs("result.ma", type="mayaAscii")
        return


if __name__ == "__main__":
    from maya import standalone

    standalone.initialize(name="python")
    unittest.main(verbosity=2, failfast=1)
