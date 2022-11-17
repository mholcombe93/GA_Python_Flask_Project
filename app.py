# Import the 'Flask' class from the 'flask' library.
from flask import Flask 
from flask import request
from flask import jsonify

#PeeWee install
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('snakes', user='matthewholcombe', password='1234', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Snake(BaseModel):
  name = CharField()
  venomous = BooleanField()

db.connect()
db.drop_tables([Snake])
db.create_tables([Snake])

Snake(name='Python', venomous=False).save()
Snake(name='King', venomous=True).save()


app = Flask(__name__)


@app.route('/snakes/', methods=['GET', 'POST'])
@app.route('/snakes/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Snake.get(Snake.id == id)))
    else:
        people_list = []
        for person in Snake.select():
            people_list.append(model_to_dict(person))
        return jsonify(people_list)

  # if request.method =='PUT':
  #   body = request.get_json()
  #   Snake.update(body).where(Snake.id == id).execute()
  #   return "Snake " + str(id) + " has been updated."

  # if request.method == 'POST':
  #   new_person = dict_to_model(Snake, request.get_json())
  #   new_person.save()
  #   return jsonify({"success": True})

  # if request.method == 'DELETE':
  #   Snake.delete().where(Snake.id == id).execute()
  #   return "Snake " + str(id) + " deleted."


@app.route('/')
def index():
  return "Hello, world!"

# @app.route('/say-hello/<name>')
# def sayHello(name):
#  return f"Hello, {name}!"

# @app.route('/get-json')
# def get_json():
#   return jsonify({
#     "name": "Garfield",
#     "hatesMondays": True,
#     "friends": ["Sheldon", "Wade", "Orson", "Squeak"]
#   })


app.run(port=5000, debug=True)
