# Import the 'Flask' class from the 'flask' library.
from flask import Flask 
from flask import request
from flask import jsonify

#PeeWee install
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model



app = Flask(__name__)


@app.route('/')
def index():
  return "Hello, world!"

@app.route('/say-hello/<name>')
def sayHello(name):
 return f"Hello, {name}!"

@app.route('/get-json')
def get_json():
  return jsonify({
    "name": "Garfield",
    "hatesMondays": True,
    "friends": ["Sheldon", "Wade", "Orson", "Squeak"]
  })


app.run(port=5000, debug=True)
