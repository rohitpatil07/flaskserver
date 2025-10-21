from flask import Flask, request,jsonify
from db.db import db_routes

app = Flask(__name__)
app.register_blueprint(db_routes, url_prefix='/db')

@app.route('/', methods=['GET'])
def hello():
	res = jsonify({'message': 'Hello from DB', 'status': 'success','code':200})
	return res  

@app.route('/health', methods=['GET'])
def health():
	res = jsonify({'message': 'DB Healthy', 'status': 'success','code':200})
	return res

@app.route('/data', methods=['GET'])
def data():
	res = jsonify({'message': 'Data retrieved', 'status': 'success','code':200})
	return res

@app.route('/unauthorized', methods=['GET'])
def unauthoried():
	res = jsonify({'message': 'Unauthorized', 'status': 'failure','code':401})
	return res,401

@app.route('/fail', methods=['GET'])
def fail():
	res = jsonify({'message': 'Something is wrong', 'status': 'failure','code':500})
	return res,500