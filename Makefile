#!/bin/sh
virtualenv --no-site-packages ./
echo "Installing dependencies to $BASE_DIR environment..."
./bin/pip install -E ./ -r ./requirements.txt

