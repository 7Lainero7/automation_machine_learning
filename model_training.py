import os
import pickle

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression



def train_model():
    X_train = []
    y_train = []
    for filename in os.listdir('train'):
        df = pd.read_csv(f'train/{filename}')
        X_train.append(df.index.values.reshape(-1, 1))
        y_train.append(df['value'].values)

    X_train = np.concatenate(X_train)
    y_train = np.concatenate(y_train)

    model = LinearRegression()
    model.fit(X_train, y_train)

    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    train_model()
