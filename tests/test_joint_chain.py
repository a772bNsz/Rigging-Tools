"""
test for maya version
"""

import unittest
import pymel.core as pm
from tools.joint_chain import joint_chain


class SampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pm.system.newFile()
        cls.curve = [
            pm.curve(
                d=3, periodic=0,
                knot=[0.0, 0.0, 0.0, 1.0, 2.0, 2.0, 2.0],
                point=[[0.0, 3.201, -3.134], [0.0, 5.112, -2.019],
                       [0.0, 8.933, 0.213], [0.0, 13.112, -1.81],
                       [0.0, 15.201, -2.821]]
            ),
        ]

    def test_joint_chain(self):
        self.assertTrue(joint_chain(self.curve, number=8),
                        "no joint chain made")

    def test_chain_name(self):
        self.assertEqual(joint_chain(self.curve, number=10, name="spine#_JNT"),
                         "spine1_JNT",
                         "did not rename or # is not 1")

    @classmethod
    def tearDownClass(cls):
        pm.system.saveAs("result.ma", type="mayaAscii")
        print "\n>>>>>", pm.system.sceneName()


if __name__ == '__main__':
    from maya import standalone, cmds

    standalone.initialize(name='python')
    cmds.loadPlugin("lookdevKit")  # not necessary if $PYMEL_SKIP_INIT=0
    unittest.main(verbosity=3, failfast=1)
