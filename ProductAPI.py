from flask import Blueprint,request
from pymongo import MongoClient
from bson.json_util import dumps


produect_api = Blueprint('produect_api', __name__)
client=MongoClient()
db=client["Project"]


@produect_api.route("/product", methods=['GET', 'POST', 'DELETE', 'PATCH'])

def allProducts():
    if request.method == 'GET':
        data = db.prodcut.find()
        return dumps(data)
