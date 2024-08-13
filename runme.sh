#!/bin/bash

echo "Installing or checking requirements"
./requirements.sh

if [ $? -ne 0 ]; then
  echo "Error while requirements.sh run"
  exit 1
fi

echo "Running transfer script"
python3 kaggle-to-postgre.py

if [ $? -ne 0 ]; then
  echo "Error while kaggle-to-postgre.py run"
  exit 1
fi

echo "Transfer was completed"
