"""This module is responsible for training a machine learning model using GridSearchCV
and automatically retraining the model every specified number of seconds."""

# Import necessary libraries
import time
import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV

# Define a function to train a model


def train_model(data, target):
    """Train a machine learning model using GridSearchCV."""
    # Split the data into training and test sets
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.2, random_state=42)

    # Create a random forest classifier
    clf = RandomForestClassifier(random_state=42)

    # Define a parameter grid for GridSearchCV
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10]
    }

    # Create a GridSearchCV object
    grid_search = GridSearchCV(clf, param_grid, cv=5)

    # Fit the GridSearchCV object to the data
    grid_search.fit(x_train, y_train)

    # Get the best estimator
    best_clf = grid_search.best_estimator_

    # Make predictions on the test set using the best estimator
    y_pred = best_clf.predict(x_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy}')

    # Print the confusion matrix
    print(f'Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}')

    # Print the classification report
    print(f'Classification Report:\n{classification_report(y_test, y_pred)}')

    # Return the best estimator
    return best_clf

# Define a function to automatically retrain the model every specified
# number of seconds


def auto_train(data, target, interval):
    """Automatically retrain the model every specified number of seconds."""
    while True:
        print('Training model...')
        model = train_model(data, target)
        print('Training complete. Waiting for next training cycle...')
        time.sleep(interval)

        # Log the model's feature importances
        logging.info('Feature importances: %s', model.feature_importances_)
