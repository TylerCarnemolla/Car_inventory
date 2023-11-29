from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, Car, User, car_schema, cars_schema


api = Blueprint('api', __name__, url_prefix='/api') #prefix means that it goes before the slug


@api.route('/cars', methods = ['POST'])
@token_required
def add_car(current_User_token):
    brand = request.json['brand']
    model = request.json['model']
    year = request.json['year']
    color = request.json['color']
    car_token = current_User_token.token

    print(f'BIG TESTER: {current_User_token.token}')

    car = Car(brand, model, year, color, car_token=car_token) #we do_User_token =_User_toked to over-write
    #the previous value for that variable

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

# this route is to bring back all cars in the inventory

@api.route('/cars', methods = ['GET'])
@token_required
def get_all_cars(current_User_token):
    a_car = current_User_token.token
    cars = Car.query.filter_by(car_token = a_car).all()
    response = cars_schema.dump(cars)
    return jsonify(response)

# this route is to bring back one specific car from the inventory
@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_a_car(current_User_token, id):
    car = Car.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)


#this route allows us to update a car in case of a mistake

@api.route('/cars/<id>', methods = ['POST', 'PUT'])
@token_required
def update_car_info(current_User_token, id):
    car = Car.query.get(id)
    car.brand = request.json['brand']
    car.model = request.json['model']
    car.year = request.json['year']
    car.color = request.json['color']
    car.car_token = current_User_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

# then if we need to delete a car from the companies inventory
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_User_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)
