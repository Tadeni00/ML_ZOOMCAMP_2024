from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load DictVectorizer
with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

# Load Logistic Regression model
with open('model2.bin', 'rb') as f_in:  # Changed from 'model1.bin' to 'model2.bin'
    model = pickle.load(f_in)

@app.route('/')
def home():
    return "Welcome to the Prediction API. Use the /predict endpoint to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    client_data = request.json
    # Transform the client data using the DictVectorizer
    X_client = dv.transform([client_data])
    # Predict the score using the model
    y_pred = model.predict(X_client)
    # Get the predicted probability for the positive class
    y_proba = model.predict_proba(X_client)[:, 1]

    return jsonify({
        'prediction': bool(y_pred[0]),
        'probability': round(float(y_proba[0]), 3)
    })

if __name__ == '__main__':
    app.run(debug=True)
