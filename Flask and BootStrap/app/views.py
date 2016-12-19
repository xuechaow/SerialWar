import redis
import json
import ast
from app import app
from flask import jsonify
from flask import render_template
# import render_template. Let other things be as they are and just edit the index function.
@app.route('/')
@app.route('/index')

def index():
	 return render_template("json_g.html",title = 'JSON')
@app.route('/network')
def networkio():
	return render_template("networkio.html",title = 'networki/o')

@app.route('/test')
def test():
	return render_template("base.html",title = 'test')

@app.route('/json_graph')
def json_test():
        return render_template("json_g.html",title = 'JSON')

@app.route('/overall')
def overall():
        return render_template("overall.html",title = 'Overall')

@app.route('/avro_graph')
def avro_test():
        return render_template("avro_g.html",title = 'AVRO')

@app.route('/thrift_graph')
def thrift_test():
        return render_template("thrift_g.html",title = 'THRIFT')

@app.route('/meanwhile')

def meanwhile():
	return render_template("meanwhile.html",title = "comparison")

@app.route('/api/<name_db>')
def get_data(name_db):
	
	redis_entry = redis.Redis(host = 'ec2-52-39-137-189.us-west-2.compute.amazonaws.com', port = 6379,db = 1 )

	if(name_db == "json"):
		data_response = redis_entry.get('bytes')
	
	if(name_db == "avro"):
		data_response = redis_entry.get('bytes_1')

	if(name_db == "thrift"):
		data_response = redis_entry.get('bytes_3')
        data_resp_dict = {"bytes":data_response} 
	return jsonify(data_resp_dict)
