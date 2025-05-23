from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import joblib

app = Flask(__name__)

# Load your model and scaler (make sure diabetes.pkl and scaler.pkl are in the same folder)
model = joblib.load('diabetes.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    # Serve the frontend HTML file
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract input features in the exact order your model expects
        features = [  
            data['pregnancies'],
            data['glucose'],
            data['bloodPressure'],
            data['skinThickness'],
            data['insulin'],
            data['bmi'],
            data['dpf'],
            data['age']
        ]

        # Convert to numpy array and reshape for scaler/model
        input_array = np.array(features).reshape(1, -1)

        # Scale input features
        scaled_input = scaler.transform(input_array)

        # Make prediction (0 = negative, 1 = positive)
        prediction = model.predict(scaled_input)[0]

        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        # In case of error, send message back
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
