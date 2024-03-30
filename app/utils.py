import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(data_path):
    data = pd.read_csv(data_path)
    X = data.iloc[:, 2:].values.astype(np.float32)  
    y = data.iloc[:, 1].map({'M': 1, 'B': 0}).values 

def preprocess_data(X):
    """
    Preprocess the dataset by applying necessary transformations.
    """
    # Separate the mean, standard error, and worst features
    mean_features = X[:, :10]
    std_error_features = X[:, 10:20]
    worst_features = X[:, 20:]

    # Normalize the features
    scaler = StandardScaler()
    mean_features = scaler.fit_transform(mean_features)
    std_error_features = scaler.transform(std_error_features)
    worst_features = scaler.transform(worst_features)

    # Concatenate the preprocessed features
    preprocessed_X = np.concatenate((mean_features, std_error_features, worst_features), axis=1)

    return preprocessed_X

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test