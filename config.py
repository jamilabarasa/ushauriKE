from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ushaurike1234560991'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ushauriKE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)