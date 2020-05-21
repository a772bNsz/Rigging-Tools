#!/bin/bash
set -e
echo ">>>>> MAYAPY"
mayapy -m tests.test_color_shapes
COPY_FROM=/root/maya/projects/default/scenes/test_color_shapes.ma
COPY_TO=results/test_color_shapes.ma
cp $COPY_FROM $COPY_TO 2>/dev/null || :
