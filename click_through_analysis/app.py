from flask import Flask, render_template, request, jsonify
import pandas as pd
from src.predict_pipeline import PredictionPipeline

app = Flask(__name__)

# Initialize the prediction pipeline
prediction_pipeline = PredictionPipeline()

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Retrieve the form data from the request
        data = {
            "Ad Topic Line": request.form["ad_topic_line"],
            "City": request.form["city"],
            "Gender": request.form["gender"],
            "Country": request.form["country"],
            "Daily Time Spent on Site": float(request.form["time_spent_on_site"]),
            "Age": int(request.form["age"]),
            "Area Income": float(request.form["area_income"]),
            "Daily Internet Usage": float(request.form["daily_internet_usage"]),
        }

        # Convert form data into a DataFrame
        df = pd.DataFrame([data])

        # Use the prediction pipeline to make predictions
        prediction = prediction_pipeline.predict(df)

         # Debugging: Print the prediction to the console
        print(f"Prediction: {prediction[0]}")

        # Decide the message based on prediction
        if prediction[0] == 1:
            result_message = "😊😀...The user clicked on Ad"
        else:
            result_message = "😥🤔...The user did not click on Ad"

        # Render result on the page
        return render_template("home.html", result_message=result_message)

    except Exception as e:
        # Handle errors and display an error message
        return render_template("home.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)