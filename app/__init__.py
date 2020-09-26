from flask import Flask
from flask_migrate import Migrate
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_jwt_extended import JWTManager

from app.commands import *
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv, find_dotenv

from config import Config

load_dotenv(find_dotenv())

app = Flask(__name__, static_folder="../static", template_folder="./views")
api = Api(app)
app.config.from_object(Config)
mongo = PyMongo(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
mail = Mail(app)

from app.commands import *
app.cli.add_command(cli_command)


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from app.routes.api import routes
from app.routes.web import routes

