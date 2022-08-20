from app import app
from app.controllers import anggotas
from flask import Blueprint, request

customers_blueprint = Blueprint('customers_router', __name__)

@app.route("/users", methods=["GET"])
def showUsers():
    return anggotas.shows()

@app.route("/user", methods=["GET"])
def showUser():
    params = request.json
    return anggotas.show(**params)

@app.route("/user/insert", methods=["POST"])
def insertUser():
    params = request.json
    return anggotas.insert(**params)

@app.route("/user/update", methods=["PUT"])
def updateUser():
    params = request.json
    return anggotas.update(**params)

@app.route("/user/delete", methods=["DELETE"])
def deleteUser():
    params = request.json
    return anggotas.delete(**params)

@app.route("/user/requesttoken", methods=["POST"])
def requestToken():
    params = request.json
    return anggotas.token(**params)