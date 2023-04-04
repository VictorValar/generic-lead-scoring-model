#!/bin/bash

clear
echo "Deleting folders..."
rm -rf build
rm -rf dist
rm -rf *.egg-info

echo "Building dist..."
python3 setup.py sdist bdist_wheel

echo "Upload to PyPI..."
twine upload dist/*

echo "Done!"