#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from model import RandomForestModel
from utils import load_data, preprocess_data, split_data

app = Flask(__name__)

# Load the dataset

path = 'data/raw/wdbc.csv'  # Add whitespace around the '=' operator
(X, y) = load_data(path)

# Preprocess the data

X = preprocess_data(X)

# Split the data into train and test sets

(X_train, X_test, y_train, y_test) = split_data(X, y)

# Train the model

model = RandomForestModel()
model.train(X_train, y_train)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:

        # Assuming data is a dictionary containing feature-value pairs
        # Extract numeric feature values from the dictionary

        features = [float(value) for value in data.values()]

        # Make prediction using the model

        prediction = model.predict([features])
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

