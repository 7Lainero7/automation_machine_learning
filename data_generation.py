import os

import numpy as np
import pandas as pd


def create_datasets():
    os.makedirs('train', exist_ok=True)
    os.makedirs('test', exist_ok=True)

    for i in range(5):
        data = np.linspace(0, 10, 100)
        noise = np.random.normal(0, 1, 100)
        anomalies = noise * np.random.choice([1, 0], size=100, p=[0.05, 0.95])
        data += noise + anomalies

        df_train = pd.DataFrame({'value': data})
        df_train.to_csv(f'train/train_data_{i}.csv', index=False)

        data_test = np.linspace(0, 10, 100)
        noise_test = np.random.normal(0, 1, 100)
        anomalies_test = noise_test * np.random.choice([1, 0], size=100, p=[0.05, 0.95])
        data_test += noise_test + anomalies_test

        df_test = pd.DataFrame({'value': data_test})
        df_test.to_csv(f'test/test_data_{i}.csv', index=False)


if __name__ == "__main__":
    create_datasets()
