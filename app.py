from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)

server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://william@localhost:5432/pets_db'

database = SQLAlchemy(server)

class Pets(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    pet_name = database.Column(database.String(20))
    breed = database.Column(database.String(20))

@server.route('/pets', methods=['GET'])
def get_pets():
    pets = Pets.query.all()
    formatted_pets = []
    for pet in pets:
        formatted_pets.append(
            {
                "id": pet.id,
                "pet_name": pet.pet_name,
                "breed": pet.breed 
            }
        )
    return jsonify(formatted_pets)

@server.route('/hounds', methods=['GET'])
def get_hounds():
    pets = Pets.query.filter(Pets.breed == 'hound')
    formatted_pets = []
    for pet in pets:
        formatted_pets.append(
            {
                "id": pet.id,
                "pet_name": pet.pet_name,
                "breed": pet.breed 
            }
        )
    return jsonify(formatted_pets)

server.run(debug=True)