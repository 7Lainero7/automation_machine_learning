import os

import pandas as pd

from sklearn.preprocessing import StandardScaler


def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    scaler = StandardScaler()
    df['value'] = scaler.fit_transform(df[['value']])
    df.to_csv(file_path, index=False)


def preprocess_datasets():
    for folder in ['train', 'test']:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            preprocess_data(file_path)


if __name__ == "__main__":
    preprocess_datasets()
