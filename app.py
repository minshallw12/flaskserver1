from flask import Flask
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)

server.config['SQLALCHEMY_DATABASE_URI'] = 