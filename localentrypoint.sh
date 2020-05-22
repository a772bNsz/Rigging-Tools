#!/bin/bash
set -e
echo ">>>>> MAYAPY"
mayapy -m tests.test_shapes
COPY_FROM=/root/maya/projects/default/scenes/test_control_shapes.ma
COPY_TO=results/test_control_shapes.ma
cp $COPY_FROM $COPY_TO 2>/dev/null || :
