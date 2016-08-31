#!/bin/bash

python_path=/usr/local/bin/python2.7

parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )

cd $parent_path

${python_path} run.py -p 8081