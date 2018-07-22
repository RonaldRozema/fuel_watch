from flask import Blueprint

bike_api = Blueprint('bike_api', __name__)

@bike_api.route('/mybike')
def get_my_bike():
    return "Yamaha R6 2006"