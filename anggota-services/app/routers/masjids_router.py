from app import app
from app.controllers import masjids
from flask import Blueprint, request

borrows_blueprint = Blueprint('masjids_router', __name__)

@app.route("/masjids", methods=["GET"])
def showBorrows():
    return masjids.shows()

@app.route("/masjids/insert", methods=["POST"])
def insertBorrow():
    params = request.json
    return masjids.add(**params)

@app.route("/masjids/status", methods=["POST"])
def chanceBorrow():
    params = request.json
    return masjids.changeStatus(**params)