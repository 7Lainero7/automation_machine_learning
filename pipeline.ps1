./venv/Scripts/activate.bat

pip install -r requirements.txt

python data_generation.py
python data_preprocessing.py
python model_training.py
python model_testing.py

./venv/Scripts/deactivate.bat
