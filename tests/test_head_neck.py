"""
test for maya version
"""

import unittest
import pymel.core as pm
from pymel import versions

maya_version = versions.current()


class SampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pm.system.newFile()

    @unittest.skipIf(20190000 != maya_version, "test_version_is_2019")
    def test_version_is_2019(self):
        self.assertEqual(20190000, maya_version)

    @unittest.skipIf(20180000 != maya_version, "test_version_is_2018")
    def test_version_is_2018(self):
        self.assertEqual(20180000, maya_version)

    @unittest.skipIf(201602 != maya_version, "test_version_is_2016sp1")
    def test_version_is_2016sp1(self):
        self.assertEqual(201602, maya_version)

    @classmethod
    def tearDownClass(cls):
        pm.system.saveAs("result.ma", type="mayaAscii")
        print "\n>>>>>", pm.system.sceneName()


if __name__ == '__main__':
    from maya import standalone, cmds
    standalone.initialize(name='python')
    cmds.loadPlugin("lookdevKit")  # not necessary if $PYMEL_SKIP_INIT=0
    unittest.main(verbosity=3)
