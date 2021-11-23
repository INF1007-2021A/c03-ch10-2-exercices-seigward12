#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import pandas as pd
import numpy as np
import os


WHINE_FILE_PATH = f'{os.getcwd()}/data/winequality-white.csv'

# TODO: Définissez vos fonctions ici
def prepare_data():
    dataset = pd.read_csv(WHINE_FILE_PATH, delimiter = ';')
    x, y = dataset[dataset.columns.difference(['quality'])], dataset['quality']

def train_models()
def main():
    x_train, x_test, y_train, y_test = prepare_data()
    print('prepare_data')

    trained_models = traine_models(x_train, y_train)
    print('Trained')

    predictions = predict_models(trained_models, x_test)
    print('predicted')

    model_performances = evaluate_models(predictions, y_test)
    print(f'Evaluated models. MSE: {model_performances}')


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    main()