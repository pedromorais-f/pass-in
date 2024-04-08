from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendee_handler import AttendeeHandler

#Creating a route for attendee and define the method
attendee_route_bp = Blueprint("attendee_route", __name__)

#POST: Method that submit a entity for the server
@attendee_route_bp.route("/events/<event_id>/register", methods=["POST"])
#Creating a attendee
def create_attendee(event_id):
    http_request = HttpRequest(body=request.json, param={'event_id': event_id})
    attendee_handler = AttendeeHandler()
    http_response = attendee_handler.register(http_request)

    return jsonify(http_response.get_body), http_response.get_status_code

#GET Method to return data requests
@attendee_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendee(attendee_id):
    http_request = HttpRequest(param={"attendee_id": attendee_id})
    attendee_handler = AttendeeHandler()
    http_responde = attendee_handler.find_attendee_badge(http_request)

    return jsonify(http_responde.get_body), http_responde.get_status_code