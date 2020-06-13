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
        pm.newFile()

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
        pm.saveAs("result.ma", type="mayaAscii")


class SampleInheritTest(SampleTest):
    @classmethod
    def setUpClass(cls):
        super(SampleInheritTest, cls).setUpClass()
        print ">>>>> SETUP"

    def test_version_is_2020(self):
        self.assertNotEqual(20200000, maya_version, "test_version_is_2020")

    @classmethod
    def tearDownClass(cls):
        super(SampleInheritTest, cls).tearDownClass()
        print ">>>>> TEARDOWN"


if __name__ == "__main__":
    from maya import standalone, cmds
    standalone.initialize(name='python')
    cmds.loadPlugin("lookdevKit")  # not necessary if $PYMEL_SKIP_INIT=0

    # unittest.main(verbosity=3, failfast=1)

    test_case = SampleInheritTest
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    runner = unittest.TextTestRunner(verbosity=3, failfast=1).run(suite)
