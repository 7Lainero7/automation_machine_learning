#!/bin/bash

python -m venv venv

source ./venv/Scripts/activate

./venv/Scripts/python -m pip install -r requirements.txt

python data_generation.py
python data_preprocessing.py
python model_training.py
python model_testing.py

deactivate
