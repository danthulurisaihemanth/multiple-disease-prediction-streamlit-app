from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Define the absolute path for the model directory
BASE_DIR = r"D:\Projects\Multiple-Disease-Prediction-App"
MODEL_DIR = os.path.join(BASE_DIR, "Saved models")

# Function to load models safely
def load_model(filename):
    try:
        with open(os.path.join(MODEL_DIR, filename), 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None

# Load models
diabetes_model = load_model('diabetes_model.sav')
heart_disease_model = load_model('heart_disease_model.sav')
parkinsons_model = load_model('parkinsons_model.sav')

# Prediction routes
def make_prediction(model, features):
    if model is None:
        return jsonify({'error': 'Model not available'}), 500
    try:
        input_data = np.array(features).reshape(1, -1)
        prediction = model.predict(input_data)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 400

@app.route('/predict/diabetes', methods=['POST'])
def predict_diabetes():
    data = request.get_json()
    return make_prediction(diabetes_model, data.get('features', []))

@app.route('/predict/heart', methods=['POST'])
def predict_heart():
    data = request.get_json()
    return make_prediction(heart_disease_model, data.get('features', []))

@app.route('/predict/parkinsons', methods=['POST'])
def predict_parkinsons():
    data = request.get_json()
    return make_prediction(parkinsons_model, data.get('features', []))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
