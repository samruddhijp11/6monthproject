from flask import Flask
from app import app as app1_blueprint
from app1 import app as app2_blueprint

app = Flask(__name__)

# Register routes from app.py
app.register_blueprint(app1_blueprint, url_prefix="/predict")

# Register routes from app1.py
app.register_blueprint(app2_blueprint, url_prefix="/risk")

if __name__ == "__main__":
    app.run()
