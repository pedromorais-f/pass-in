from flask import Flask
from flask_cors import CORS
from src.main.routes.events_routes import event_route_bp
from src.models.settings.connection import connection_handler
from src.main.routes.attendees_routes import attendee_route_bp
from src.main.routes.check_ins_routes import check_in_route_bp

#Connecting with database
connection_handler.connect_to_db()

#Creating the application
app = Flask(__name__)
CORS(app)

#Registering an event route for the application
app.register_blueprint(event_route_bp)
#Registering an attendee route for the application
app.register_blueprint(attendee_route_bp)
#Registering a check in route for the application
app.register_blueprint(check_in_route_bp)