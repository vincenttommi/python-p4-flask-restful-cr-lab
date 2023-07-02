#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Plants(Resource):
    def get(self):
        plants = Plant.query.all()
        response_body = [plant.to_dict() for plant in plants]

        response = make_response(
            jsonify(response_body),
            200
        )

        return response
    
    def post(self):
        request_body = request.get_json()

        new_plant = Plant(
            name=request_body.get('name'),
            image=request_body.get('image'),
            price=request_body.get('price')
        )

        db.session.add(new_plant)
        db.session.commit()

        response = make_response(
            jsonify(new_plant.to_dict()),
            201
        )

        return response

api.add_resource(Plants, '/plants')

class PlantByID(Resource):
    def get(self, id):
        plant = Plant.query.get(id)
        
        if plant is None:
            response_body = {
                "error": "Plant not found"
            }
            response_code = 404
        else:
            response_body = plant.to_dict()
            response_code = 200

        response = make_response(
            jsonify(response_body),
            response_code
        )

        return response

api.add_resource(PlantByID, '/plants/<int:id>')
        
if __name__ == '__main__':
    app.run(port=5555, debug=True)