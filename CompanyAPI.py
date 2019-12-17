from flask import Blueprint,request,jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json


comapny_api = Blueprint('comapny_api', __name__)
client=MongoClient()
db=client["Project"]


@comapny_api.route("/company", methods=['GET'])
def allComapny():
    data = db.Company.find()
    response = []
    for document in data:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

@comapny_api.route("/company/<id>", methods=['GET'])
def companyby_Id(id):
    data = db.Company.find_one({'_id': ObjectId(id)})
    data['_id'] = str(data['_id'])
    return dumps(data)

@comapny_api.route("/company", methods=['POST'])
def createCompany():
    data = request.get_json()
    del data["_id"]
    db.Company.insert_one(data)
    page_sanitized = json.loads(dumps(data))
    return jsonify({'ok': True, 'message': 'User created successfully!','result': page_sanitized}) , 200

@comapny_api.route("/company", methods=['PUT'])
def updateCompany():
    data = request.get_json()
    data["_id"] = ObjectId(data["_id"])
    db.Company.save(data)
    page_sanitized = json.loads(dumps(data))
    return jsonify({'ok': True, 'message': 'User updated successfully!', 'result': page_sanitized}), 200

@comapny_api.route("/company/<id>", methods=['DELETE'])
def delete_company(id):
    db.Company.delete_one({'_id': ObjectId(id)})
    resp = jsonify('User deleted successfully!')
    resp.status_code = 200
    return resp

