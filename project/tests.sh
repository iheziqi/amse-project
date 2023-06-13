#! /bin/bash

# Actives the virtual env
# source ../env/bin/active
cd data

# Executes test
echo "===== Tests start ====="
python test.py
echo "===== Tests end ====="

# Terminates the virtual env
# deactive