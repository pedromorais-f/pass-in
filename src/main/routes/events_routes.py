from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest

#Creating a route for event and define the method
event_route_bp = Blueprint("event_route", __name__)

#POST: Method that submit a entity for the server
@event_route_bp.route("/events", methods=["POST"])
#Creating a event
def create_event():
    http_request = HttpRequest(request.json)

    return jsonify({ 'ola': 'mundo' }), 200