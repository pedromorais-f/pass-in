from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendee_handler import AttendeeHandler
from src.errors.error_handler import error_handler

#Creating a route for attendee and define the method
attendee_route_bp = Blueprint("attendee_route", __name__)

#POST: Method that submit a entity for the server
@attendee_route_bp.route("/events/<event_id>/register", methods=["POST"])
#Creating a attendee
def create_attendee(event_id):
    try:
        http_request = HttpRequest(body=request.json, param={'event_id': event_id})
        attendee_handler = AttendeeHandler()
        http_response = attendee_handler.register(http_request)
    except Exception as exception:
        http_response = error_handler(exception)

    return jsonify(http_response.get_body), http_response.get_status_code

#GET Method to return data requests
@attendee_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendee(attendee_id):
    try:
        http_request = HttpRequest(param={"attendee_id": attendee_id})
        attendee_handler = AttendeeHandler()
        http_response = attendee_handler.find_attendee_badge(http_request)
    except Exception as exception:
        http_response = error_handler(exception)

    return jsonify(http_response.get_body), http_response.get_status_code

#GET Method to return data requests
@attendee_route_bp.route("/events/<event_id>/badges", methods=["GET"])
def get_attendees(event_id):
    try:
        http_request = HttpRequest(param={"event_id": event_id})
        attendee_handler = AttendeeHandler()
        http_response = attendee_handler.find_attnedees_from_event(http_request)
    except Exception as exception:
        http_response = error_handler(exception)

    return jsonify(http_response.get_body), http_response.get_status_code