"""This module is responsible for creating and training machine learning models."""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


class Model:
    def __init__(self, dataset):
        self.dataset = dataset

    def train(self):
        y = self.dataset.Price
        feature_columns = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
        X = self.dataset[feature_columns]
        train_x, val_x, train_y, val_y = train_test_split(X, y, random_state=0)
        model = RandomForestRegressor(random_state=1)
        model.fit(train_x, train_y)
        val_predictions = model.predict(val_x)
        print(mean_absolute_error(val_y, val_predictions))