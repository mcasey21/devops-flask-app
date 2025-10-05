#!/bin/bash

# update and upgrade packages
sudo apt update && sudo apt upgrade -y

# install packages
sudo apt install -y nano vim python-is-python3 python3-venv python3-pip

# create and activate virtual environment
python -m venv .my_venv
source .my_venv/bin/activate

# install flask
pip install flask

# run flask app in background
# listening on all interfaces
flask --app hello run --host=0.0.0.0 &
