from flask import Blueprint,request
from pymongo import MongoClient
from bson.json_util import dumps


account_api = Blueprint('account_api', __name__)
client=MongoClient()
db=client["Project"]


@account_api.route("/account", methods=['GET', 'POST', 'DELETE', 'PATCH'])

def accountList():
    if request.method == 'GET':
        data = db.Company.find()
        return dumps(data)
