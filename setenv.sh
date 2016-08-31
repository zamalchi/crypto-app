#!/bin/bash

module add engaging/python/2.7.10

pip show -q passlib

if [ $? -eq 1 ]; then
	pip install --user passlib
fi
