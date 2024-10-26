import pickle

# Load DictVectorizer
with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

# Load Logistic Regression model
with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)


## Test Model ##


# Define the client data
client_data = {"job": "management", "duration": 400, "poutcome": "success"}

# Transform the client data using the DictVectorizer
X = dv.transform([client_data])

# Predict the score using the model
y_pred = model.predict(X)

# Get the predicted probability for the positive class
y_proba = model.predict_proba(X)[:, 1]

print(f"Prediction (0: negative, 1: positive): {y_pred[0]}")
print(f"Predicted probability of positive class: {y_proba[0]:.3f}")