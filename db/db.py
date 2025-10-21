from flask import Blueprint, Flask,jsonify

db_routes = Blueprint('db_routes', __name__)

@db_routes.route('/', methods=['GET'])
def dbhello():
	res = jsonify({'message': 'DB Routes', 'status': 'success','code':200})
	return res ,200

@db_routes.route('/health', methods=['GET'])
def dbhealth():
	res = jsonify({'message': 'Healthy', 'status': 'success','code':200})
	return res,200

@db_routes.route('/data', methods=['GET'])
def dbdata():
	res = jsonify({'message': 'Data retrieved', 'status': 'success','code':200})
	return res,200

@db_routes.route('/users', methods=['GET'])
def dbusers():
	users = [{
		'id': 1,
		'name': 'John Doe'
	},{
		'id': 2,
		'name': 'Jane Smith'
	}]

	res = jsonify({'message': 'User Data retrieved', 'status': 'success','code':200,"users": users})
	return res ,200

@db_routes.route('/tables', methods=['GET'])
def dbtables():
	tables = ['users', 'orders', 'products','matchres']
	res = jsonify({'message': 'Table Data Received', 'status': 'success','code':200, "tables": tables})
	return res,200

@db_routes.route('/matchres', methods=['GET'])
def dbmatchres():
	matchres = [
		{'match_id': 1, 'team_a': 'Barcelona', 'team_b': 'Real Madrid', 'score_a': 3, 'score_b': 2},
		{'match_id': 2, 'team_a': 'Barcelona', 'team_b': 'Atletico Madrid', 'score_a': 1, 'score_b': 1},
	]
	res = jsonify({'message': 'Match  results received', 'status': 'success','code':200,"matchres": matchres})
	return res,200