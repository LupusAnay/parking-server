import base64

from flask.views import MethodView
from flask import Blueprint, request, make_response, jsonify
from project.models import Customer, Order
from project import db

parking_blueprint = Blueprint('parking', __name__)


class RegisterAPI(MethodView):
    @staticmethod
    def post():
        params = {} if request.get_json() is None else request.get_json()
        params_list = ['car_id', 'first_name', 'second_name',
                       'address', 'phone', 'user_pic']

        for param in params:
            if param in params_list:
                params_list.remove(param)

        if len(params_list) > 0 or params['user_pic'] is None:
            response = {
                'not_provided': params_list,
                'what': 'Please, provide params or picture',
                'result': 'error'
            }
            return jsonify(response), 200

        image = open('images/' + params['car_id'] + '.png', 'wb')
        image.write(base64.b64decode(params['user_pic']))
        image = open('images/' + params['car_id'] + '.b64', 'w')
        image.write(params['user_pic'])

        user = Customer.query.filter_by(car_id=params['car_id']).first()
        if not user:
            try:
                user = Customer(params.get('car_id'),
                                params.get('first_name'),
                                params.get('second_name'),
                                params.get('address'),
                                params.get('phone'))
                db.session.add(user)
                db.session.commit()

                response = {
                    'result': 'success',
                    'what': 'User successfully added'
                }
                return make_response(jsonify(response)), 200
            except Exception as e:
                response = {
                    'result': 'error',
                    'what': 'Unexpected error'
                }
                return make_response(jsonify(response)), 500
        else:
            response = {
                'result': 'error',
                'what': 'User already exists',
            }
            return make_response(jsonify(response)), 202

    @staticmethod
    def get():
        car_id = request.args.get('car_id')
        if not car_id:
            response = {
                'result': 'error',
                'what': 'Please, provide car_id'
            }
            return make_response(jsonify(response)), 400

        user = Customer.query.filter_by(car_id=car_id).first()
        if not user:
            response = {
                'result': 'error',
                'what': 'User does not exist'
            }
            return make_response(jsonify(response)), 202
        else:
            try:
                image = open('images/' + car_id + '.b64', 'r')
                encoded_image = image.read()
            except FileNotFoundError as e:
                print("Все сломалось")
                encoded_image = 'null'
            orders = Order.query.filter_by(car_id=car_id).all()
            orders = [order.as_dict() for order in orders]
            user = user.as_dict()
            response = jsonify({
                'user_data': user,
                'user_pic': encoded_image,
                'orders': orders
            })
            return response, 200


class ReserveAPI(MethodView):
    def get(self):
        return 'Reserve'


class PlacesAPI(MethodView):
    def get(self):
        return 'Places'


class SearchAPI(MethodView):
    def get(self):
        return 'search'


registration_view = RegisterAPI.as_view('register_api')
reserve_view = ReserveAPI.as_view('login_api')
places_view = PlacesAPI.as_view('places_api')
search_view = SearchAPI.as_view('search_api')

parking_blueprint.add_url_rule(
    '/users',
    view_func=registration_view,
    methods=['POST', 'GET']
)

parking_blueprint.add_url_rule(
    '/reserve',
    view_func=reserve_view,
    methods=['GET', 'POST']
)

parking_blueprint.add_url_rule(
    '/places',
    view_func=places_view,
    methods=['GET', 'POST']
)

parking_blueprint.add_url_rule(
    '/search',
    view_func=search_view,
    methods=['GET', 'POST']
)
