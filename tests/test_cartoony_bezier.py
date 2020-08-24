import unittest
import pymel.core as pm
from tools.cartoony_bezier import Rig


class TestMayaFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">>>>> SETUP"

        cls.cartoony_bezier = Rig()

    def setUp(self):
        pm.newFile(f=1)

        filenames = ["bezier_limb"]
        self.cartoony_bezier.import_maya_files(filenames)

    def test_connect(self):
        params = {
            "start": "joint1",
            "middle": "joint2",
            "end": "joint3",
        }
        connected = self.cartoony_bezier.connect(**params)

        self.assertTrue(connected, "connection failed")

    @classmethod
    def tearDownClass(cls):
        pm.saveAs("result.ma", type="mayaAscii")
        print ">>>>> TEARDOWN"


if __name__ == "__main__":
    from maya import standalone, cmds

    standalone.initialize(name="python")
    cmds.loadPlugin("lookdevKit")

    unittest.main(verbosity=2, failfast=1)

    # test_case = TestCartoonyBezier
    # suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    # unittest.TextTestRunner(verbosity=2, failfast=1).run(suite)
