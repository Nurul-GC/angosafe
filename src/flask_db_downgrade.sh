#! /usr/bin/bash
cd ./
export FLASK_APP='index.py'
/usr/bin/python3 -m flask db downgrade