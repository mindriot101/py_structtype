#!/usr/bin/env sh

set -e

conda install pytest
pip install tox ctox
pip install -e .
