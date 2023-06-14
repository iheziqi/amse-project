#! /bin/bash

# Actives the virtual env
pip install -r requirements.txt
cd data

# Executes test
echo "===== Tests start ====="
python test.py
echo "===== Tests end ====="
