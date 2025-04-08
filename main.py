# main.py
from flask import Flask
from app import app as risk_app
from app1 import app as diabetes_app

app = Flask(__name__)

# Register both apps as blueprints
app.register_blueprint(risk_app, url_prefix='/risk')
app.register_blueprint(diabetes_app, url_prefix='/diabetes')

if __name__ == '__main__':
    app.run(debug=True)
