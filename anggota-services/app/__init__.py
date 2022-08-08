from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)

from app.routers.anggotas_router import *
from app.routers.masjids_router import *

app.register_blueprint(customers_blueprint)
app.register_blueprint(borrows_blueprint)