from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

client=MongoClient()
db=client["Project"]

app=Flask(__name__)

@app.route('/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def user():
    if request.method == 'GET':
        data = db.Company.find()
        return dumps(data)

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

@app.route("/edit_contact", methods = ['PUT'])
def edit_contact():
    data = json.loads(request.data)

    status = db.Company.save({
        "_id" : ObjectId(data['id']),
        "companyname" : data['companyname'],
        "companyid" : data["companyid"],
        "email" : data["email"],
        "address" : data["address"]
    })
    return dumps({'message' : 'SUCCESS'})

@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
	db.Company.delete_one({'_id': ObjectId(id)})
	resp = jsonify('User deleted successfully!')
	resp.status_code = 200
	return resp

if __name__=='__main__':
    app.run(debug=True)