from app.models.masjids import database
from app.models.anggotas import database as userdb
from flask import Flask, jsonify, request
from flask_jwt_extended import *
import json, datetime, requests

mysqldb = database()
userdb = userdb()

@jwt_required()
def shows():
    params = get_jwt_identity()
    dbresult = mysqldb.showmasjidByEmail(**params)
    result = []
    if dbresult is not None:
        for items in dbresult:
            id = json.dumps({"id":items[5]})
            instansidetail = getInstansiById(id)
            print(instansidetail)
            user = {
                "nama" : items[0],
                "namamasjid" : items[2],
                "namainstansi" : items[5],
                "provinsi" : instansidetail['provinsi'],
                "kota" : instansidetail['kota'],
                "kecamatan": instansidetail['kecamatan']
            }
            result.append(user)
    else:
        result=dbresult
        
    return jsonify(result)

@jwt_required()
def add(**params):
    token = get_jwt_identity()
    userid = userdb.showUserByEmail(**token)[0]
    namamasjid = params["namamasjid"]
    alamat = params["alamat"]
    id = json.dumps({"id":params["idinstansi"]})
    namainstansi = getInstansiById(id)["namainstansi"]
    params.update({"userid":userid,
                    "namamasjid" :namamasjid,
                    "alamat" :alamat,
                    "namainstansi" : namainstansi,
                    "isactive": 1
                })
    mysqldb.insertmasjid(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})

@jwt_required()
def changeStatus(**params):
    mysqldb.updateBorrowStatus(**params)
    mysqldb.dataCommit()
    return jsonify({"message":"Success"})
    

def getInstansiById(data):
    instansi_data = requests.get(url="http://localhost:8000/instansibyid",data=data)
    return instansi_data.json()
