# main.py
from flask import Flask
from app import app as risk_app
from app1 import app as diabetes_app
import os

app = Flask(__name__)
app.register_blueprint(risk_app, url_prefix='/risk')
app.register_blueprint(diabetes_app, url_prefix='/diabetes')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
