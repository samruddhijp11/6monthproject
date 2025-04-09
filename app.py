# app.py
from flask import Flask, render_template, request, Blueprint
import joblib
import numpy as np
from flask_cors import CORS

# app = Flask(__name__)
app = Blueprint('risk_app', __name__, template_folder='templates')
CORS(app)

# Load the trained model
model3 = joblib.load('diabetes_risk_model.pkl')

# Encode categorical variables
def encode_input(data):
    # Define the mappings used during training
    encoding_maps = {
        'gender': {'Male': 0, 'Female': 1},
        'family_history': {'No': 0, 'Yes': 1},
        'gestational_diabetes': {'No': 0, 'Yes': 1},
        'hypertension': {'No': 0, 'Yes': 1},
        'heart_disease': {'No': 0, 'Yes': 1},
        'high_blood_pressure': {'No': 0, 'Yes': 1},
        'smoking': {'Never smoked': 0, 'Currently a smoker': 1, 'Former smoker': 2},
        'alcohol': {'No': 0, 'Yes': 1},
        'sleep_pattern': {'Regular': 0, 'Irregular': 1},
        'frequent_urination': {'No': 0, 'Yes': 1},
        'blurred_vision': {'No': 0, 'Yes': 1},
        'increase_thirst': {'No': 0, 'Yes': 1},
        'unplanned_weight_loss': {'No': 0, 'Yes': 1},
        'swelling_of_legs': {'No': 0, 'Yes': 1},
        'fatigue': {'No': 0, 'Yes': 1}
    }
    
    # Apply mappings to convert categorical data to numeric
    for feature, mapping in encoding_maps.items():
        data[feature] = mapping[data[feature]]
    
    # Convert family_relation (comma-separated string) to count of relations as a simple encoding
    data['family_relation'] = len(data['family_relation'].split(',')) if data['family_relation'] else 0
    
    return np.array([list(data.values())])

# Route for the homepage
@app.route('/')
def index():
    return render_template('index1.html')

# Route for handling the form submission
@app.route('/risk/predict3', methods=['POST'])
def predict():
    # Get form data and prepare it in a dictionary
    data = {
        'age': int(request.form['age']),
        'weight': float(request.form['weight']),
        'gender': request.form['gender'],
        'family_history': request.form['family_history'],
        'family_relation': ','.join(request.form.getlist('family_relation')),
        'gestational_diabetes': request.form.get('gestational_diabetes', 'No'),
        'hypertension': request.form['hypertension'],
        'heart_disease': request.form['heart_disease'],
        'high_blood_pressure': request.form['high_blood_pressure'],
        'smoking': request.form['smoking'],
        'alcohol': request.form['alcohol'],
        'sleep_pattern': request.form['sleep_pattern'],
        'frequent_urination': 'Yes' if 'frequent_urination' in request.form else 'No',
        'blurred_vision': 'Yes' if 'blurred_vision' in request.form else 'No',
        'increase_thirst': 'Yes' if 'increase_thirst' in request.form else 'No',
        'unplanned_weight_loss': 'Yes' if 'unplanned_weight_loss' in request.form else 'No',
        'swelling_of_legs': 'Yes' if 'swelling_of_legs' in request.form else 'No',
        'fatigue': 'Yes' if 'fatigue' in request.form else 'No'
    }
    
    # Encode data
    input_data = encode_input(data)
    
    # Predict using the model
    prediction = model3.predict(input_data)[0]
    
     # Map prediction to risk labels
    risk_label = "Low Risk" if prediction == 1 else "High Risk"
    
    # Render the result page with the risk label
    return render_template('index1.html', prediction=risk_label)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
