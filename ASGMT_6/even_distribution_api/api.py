from flask import Flask, jsonify, request
from sql_connector import DatabaseConnector
from database_credentials import database_credentials

app = Flask(__name__)
database = database_credentials
db_connector = DatabaseConnector(database["db_name"], database["db_user"], database["db_password"], database["db_host"], database["db_port"])

@app.route('/', methods=['GET'])
def hello():
    res = db_connector.connect_to_db("SELECT * FROM even_distribution;", False)
    return jsonify({'data': res})


@app.route('/loans', methods=['GET'])
def loans():
    res = db_connector.connect_to_db("SELECT * FROM loans;", False)
    return jsonify({'data': res})


@app.route('/greet', methods=['POST'])
def greet():
    name = request.json['name']
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(port=3000)