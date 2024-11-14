import joblib

class PredictionPipeline:
    def __init__(self):
        # Load the preprocessor (transformer) and model
        self.column_transformer = joblib.load("artifacts/transformer.pkl")
        self.model = joblib.load("artifacts/model.pkl")

    def transform(self, X):
          # Transform the input data using the column transformer
        return self.column_transformer.transform(X)

    def predict(self, X):
        # First, transform the data, then predict using the model
        X_transformed = self.transform(X)
        prediction = self.model.predict(X_transformed)
        return prediction
