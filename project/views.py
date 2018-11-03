from flask.views import MethodView
from flask import Blueprint

parking_blueprint = Blueprint('parking', __name__)


class RegisterAPI(MethodView):
    def get(self):
        pass


class ReserveAPI(MethodView):
    def get(self):
        pass


class PlacesAPI(MethodView):
    def get(self):
        pass


registration_view = RegisterAPI.as_view('register_api')
reserve_view = ReserveAPI.as_view('login_api')
places_view = PlacesAPI.as_view('places_api')

parking_blueprint.add_url_rule(
    '/register',
    view_func=registration_view,
    methods=['GET']
)

parking_blueprint.add_url_rule(
    '/reserve',
    view_func=reserve_view,
    methods=['GET']
)

parking_blueprint.add_url_rule(
    '/places',
    view_func=places_view,
    methods=['GET']
)
