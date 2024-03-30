import pickle
from sklearn.ensemble import RandomForestClassifier

class RandomForestModel:
    def __init__(self, model_path=None):
        if model_path:
            self.model = pickle.load(open(model_path, 'rb'))
        else:
            self.model = RandomForestClassifier()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save_model(self, model_path):
        pickle.dump(self.model, open(model_path, 'wb'))