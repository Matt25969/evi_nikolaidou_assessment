from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
user=os.getenv('MYSQL_USER')
password=os.getenv('MYSQL_PASSWORD')
db=os.getenv('MYSQL_DATABASE')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.246.36.175/evie'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.189.86.80/evie'
db=SQLAlchemy

app.config['SECRET_KEY'] = 'aa9538c8f0694b22a4e473eeb5414d27'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
