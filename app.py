from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()

# Get the port from the environment variable
app.config['DEBUG'] = os.getenv('FLASK_DEBUG')  

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
