from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

client=MongoClient()
db=client["Project"]

app=Flask(__name__)

@app.route("/add_contact", methods = ['POST'])
def add_contact():
    data = json.loads(request.data)

    status = db.Company.insert_one({
        "companyname" : data['companyname'],
        "companyid" : data["companyid"],
        "email" : data["email"],
        "address" : data["address"]
    })
    return dumps({'message' : 'SUCCESS'})
