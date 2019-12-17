from flask import Flask
from AccountAPI import account_api
from CompanyAPI import comapny_api
from ProductAPI import  produect_api
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(account_api)
app.register_blueprint(comapny_api)
app.register_blueprint(produect_api)
CORS(app)
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()