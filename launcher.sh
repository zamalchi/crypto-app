#!/bin/bash

python_path=/usr/bin/python

parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )

cd $parent_path

${python_path} run.py -a 172.16.1.254 -p 40000
