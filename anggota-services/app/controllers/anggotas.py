from app.models.anggotas import database
from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import *
import json, datetime

mysqldb = database()

# @jwt_required()
def shows():
    dbresult = mysqldb.showUsers()
    result = []
    print(dbresult)
    for items in dbresult:
        user = {
            "id" : items[0],
            "nama" : items[1],
            "nia": items[2],
            "tempat_lahir": items[3],
            "tgl_lahir" : items[4],
            "image": items[5],
            "alamat" : items[6],
            "jenis_kelamin" : items[7],
            "email" : items[8]            
        }
        result.append(user)
        
    return jsonify({"user":result})

def show(**params):
    dbresult = mysqldb.showUserById(**params)
    user = {
        "id" : dbresult[0],
        "nama" : dbresult[1],
        "nia": dbresult[2],
        "tempat_lahir": dbresult[3],
        "tgl_lahir" : dbresult[4],
        "image": dbresult[5],
        "alamat" : dbresult[6],
        "jenis_kelamin" : dbresult[7],
        "email" : dbresult[8]            
    }
        
    return jsonify(user)

def insert(**params):
    mysqldb.insertUser(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

def update(**params):
    mysqldb.updateUserById(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

def delete(**params):
    mysqldb.deleteUserById(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

def token(**params):
    dbresult = mysqldb.showUserByEmail(**params)
    if dbresult is not None:
        user = {
            "nama" : dbresult[1],
            "nia": dbresult[2],
            "tempat_lahir": dbresult[3],
            "tgl_lahir": dbresult[4],
            "image": dbresult[5],
            "alamat": dbresult[6],
            "jenis_kelamin": dbresult[7],
            "email" : dbresult[8]            
        }
        expires = datetime.timedelta(days=1)
        # expires_refresh = datetime.timedelta(days=3)
        access_token = create_access_token(user, fresh=True, expires_delta=expires)
        
        data = {
            "data": user,
            "token_access": access_token
        }
        return make_response(jsonify(data),200)
    else:
        data = {
            "message":"Email tidak terdaftar"
        }
        return make_response(jsonify(data),400)
        
    # return jsonify(data)