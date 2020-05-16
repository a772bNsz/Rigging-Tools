#!/bin/bash
set -e
echo ">>>>> MAYAPY"
mayapy -m tests.test_control_shapes
COPY_FROM=/root/maya/projects/default/scenes/result.ma
COPY_TO=tests/ma/result.ma
cp $COPY_FROM $COPY_TO 2>/dev/null || :
