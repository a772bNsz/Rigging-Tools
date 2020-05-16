#!/bin/bash
set -e
echo ">>>>> MAYAPY"

# discovers tests, runs from import
#mayapy -m unittest discover -s tests -p "test_*.py" -vvv
#cp /root/workdir/tools/ma/measure_wheel.ma tools/ma/measure_wheel.ma

# run from main
for f in $(pwd)/tests/test_*.py; do
  mayapy $f
done
