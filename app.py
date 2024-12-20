from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('churn_model_pipeline.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.get_json(force=True)

    # Convert data into DataFrame
    input_data = pd.DataFrame(data)

    # Make prediction
    predictions = model.predict(input_data)

    # Send back the predictions as JSON
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
