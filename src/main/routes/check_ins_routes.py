from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_in_handler import CheckInHandler

#Creating a route for check in and define the method
check_in_route_bp = Blueprint("check_in_route", __name__)

#POST: Method that submit a entity for the server
@check_in_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
#Creating a check in
def create_check_in(attendee_id):
    http_request = HttpRequest(param={"attendee_id_info" : attendee_id})
    event_handler = CheckInHandler()
    http_response = event_handler.register(http_request)

    return jsonify(http_response.get_body), http_response.get_status_code