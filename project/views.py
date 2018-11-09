from flask.views import MethodView
from flask import Blueprint, request, make_response, jsonify
from project.models import Customer, Order
from project import db

parking_blueprint = Blueprint('parking', __name__)


class RegisterAPI(MethodView):
    def get(self):
        params = request.args
        user = Customer.query.filter_by(car_id=params.get('car_id'))
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
                'message': 'User already exists',
            }
            return make_response(jsonify(response)), 202

    def post(self):
        pass


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
    '/register',
    view_func=registration_view,
    methods=['GET', 'POST']
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
