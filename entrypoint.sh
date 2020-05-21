#!/bin/bash
set -e
echo ">>>>> MAYAPY"
for f in "$(pwd)"/tests/test_*.py; do
  mayapy -m tests."$(basename "$f")"
done
