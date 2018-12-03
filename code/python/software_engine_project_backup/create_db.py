# coding=utf-8


from app import app
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test_market:GrZFWfSh4GTMRBFy@119.23.36.18:3306/test_market'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)
