from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model and scaler
model = pickle.load(open('diabetes_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/predict1', methods=['POST'])
def predict1():
    data = request.get_json(force=True)
    gender = 1 if data['gender'] == 'M' else 0
    age = float(data['age'])
    fbs = float(data['fbs'])
    ppbs = float(data['ppbs'])
    hba1c = float(data['hba1c'])
    bmi = float(data['bmi'])
    weight = float(data['weight'])
    bps = float(data['bps'])
    bpd = float(data['bpd'])

    features = np.array([[gender, age, fbs, ppbs, hba1c, bmi, weight, bps, bpd]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)

    output = 'Diabetic' if prediction[0] == 1 else 'Non-Diabetic'

    return jsonify({'prediction': output})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
