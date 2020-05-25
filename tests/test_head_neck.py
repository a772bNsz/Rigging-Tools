"""
test for maya version
"""

import unittest
import pymel.core as pm
from pymel.util.path import path


class HeadNeckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pm.newFile()

    @classmethod
    def tearDownClass(cls):
        pm.system.saveAs("result.ma", type="mayaAscii")
        print "\n>>>>>", pm.system.sceneName()


if __name__ == '__main__':
    from maya import standalone, cmds

    standalone.initialize(name='python')
    cmds.loadPlugin("lookdevKit")  # not necessary if $PYMEL_SKIP_INIT=0
    unittest.main(verbosity=3, failfast=1)
