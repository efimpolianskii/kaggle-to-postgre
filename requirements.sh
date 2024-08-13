#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3 python3-pip

pip3 install kaggle

pip3 install pandas sqlalchemy zipfile36

pip3 freeze | grep -E 'kaggle|pandas|sqlalchemy|zipfile36'

echo "All necessary packages were installed"
