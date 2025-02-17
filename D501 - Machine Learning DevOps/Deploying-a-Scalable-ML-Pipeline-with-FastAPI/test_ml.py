import sys
import os
import pytest
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import (
    load_model,
    train_model,
)
path = "./model/model.pkl"
# Load the census.csv data
project_path = "/home/pinagm/dev/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
data_path = os.path.join(project_path, "data", "census.csv")
print(data_path)
data = pd.read_csv(data_path)

def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

# Test if an ML function returns the expected type of result
def test_load_data():
    """
    Test if the load_data function returns a RandomForestClassifier
    """
    model = load_model(path)
    assert isinstance(model, RandomForestClassifier)

# Test if the ML model uses the expected algorithm
def test_train_model():
    """
    Test if the train_model function returns a RandomForestClassifier
    """
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    # DO NOT MODIFY
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    # Use the process_data function provided to process the data
    X_train, y_train, encoder, lb = process_data(
        train,
        categorical_features=cat_features,
        label="salary",
        training=True
    )
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)

# Test if the training and test datasets have the expected size or data type
def test_data_size():
    """
    Test if the training and test datasets have the expected size
    """
    model = load_model(path)
    assert isinstance(model, RandomForestClassifier)
    # Assuming you have access to the training and test data separately
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    assert len(train_data) > 0
    assert len(test_data) > 0
    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)