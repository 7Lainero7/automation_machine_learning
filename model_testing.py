import os
import pickle

import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error


def test_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    X_test = []
    y_test = []
    for filename in os.listdir('test'):
        df = pd.read_csv(f'test/{filename}')
        X_test.append(df.index.values.reshape(-1, 1))
        y_test.append(df['value'].values)

    X_test = np.concatenate(X_test)
    y_test = np.concatenate(y_test)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')


if __name__ == "__main__":
    test_model()
