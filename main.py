from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	res = jsonify({'message': 'Hello World v2', 'status': 'success','code':200})
	return res  

@app.route('/health', methods=['GET'])
def health():
	res = jsonify({'message': 'Healthy', 'status': 'success','code':200})
	return res

@app.route('/data', methods=['GET'])
def data():
	res = jsonify({'message': 'Data retrieved', 'status': 'success','code':200})
	return res

@app.route('/unauthorized', methods=['GET'])
def unauthoried():
	res = jsonify({'message': 'Unauthorized', 'status': 'failure','code':401})
	return res

@app.route('/fail', methods=['GET'])
def fail():
	res = jsonify({'message': 'Something is wrong', 'status': 'failure','code':500})
	return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)