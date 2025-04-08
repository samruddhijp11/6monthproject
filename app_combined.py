from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # to allow cross-origin requests (important for GitHub Pages)

# Load both models
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))
risk_model = pickle.load(open('diabetes_risk_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return "Backend is Running!"

# Route for diabetes prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([
        data['Gender'],
        data['Age'],
        data['FBS'],
        data['PPBS'],
        data['HbA1c'],
        data['BMI'],
        data['Weight'],
        data['BP_Systolic'],
        data['BP_Diastolic']
    ]).reshape(1, -1)
    scaled = scaler.transform(features)
    prediction = diabetes_model.predict(scaled)
    return jsonify({'result': int(prediction[0])})

# Route for risk calculation
@app.route('/risk', methods=['POST'])
def risk():
    data = request.get_json()
    input_data = np.array([
        data['Age'],
        data['Gender'],
        data['Weight'],
        data['Family_History'],
        data['Gestational'],
        data['Chronic'],
        data['Smoking'],
        data['Alcohol'],
        data['Sleep'],
        data['Frequent_Urination'],
        data['Increased_Thirst'],
        data['Weight_Loss'],
        data['Blurred_Vision'],
        data['Fatigue'],
        data['Swelling']
    ]).reshape(1, -1)
    prediction = risk_model.predict(input_data)
    return jsonify({'risk_level': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
