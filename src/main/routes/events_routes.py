from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler
from src.errors.error_handler import error_handler

#Creating a route for event and define the method
event_route_bp = Blueprint("event_route", __name__)

#POST: Method that submit a entity for the server
@event_route_bp.route("/events", methods=["POST"])
#Creating a event
def create_event():
    try:
        http_request = HttpRequest(request.json)
        event_handler = EventHandler()
        http_response = event_handler.register(http_request)
    except Exception as exception:
        http_response = error_handler(exception)
    
    return jsonify(http_response.get_body), http_response.get_status_code

#GET Method to return data requests
@event_route_bp.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    try:
        http_request = HttpRequest(param={"event_id": event_id})
        event_handler = EventHandler()
        http_response = event_handler.find_event_by_id(http_request)
    except Exception as exception:
        http_response = error_handler(exception)
    
    return jsonify(http_response.get_body), http_response.get_status_code