from flask import Flask
from flask_cors import CORS
from src.main.routes.events_routes import event_route_bp

#Creating the application
app = Flask(__name__)
CORS(app)

#Registering a event route for the application
app.register_blueprint(event_route_bp)