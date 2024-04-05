from typing import Dict
from src.models.settings.connection import connection_handler
from src.models.entities.events import Events

#Class that will make actions in the database
class EventsRepository:
    
    #Method to insert a Event in the database
    def insert_event(eventsInfo:Dict) -> Dict:
        with connection_handler as db_connection:
            event = Events(
                id = eventsInfo.get('uuid'),
                title = eventsInfo.get('title'),
                details = eventsInfo.get('details'),
                slug = eventsInfo.get('slug'),
                maximum_attendees = eventsInfo.get('maximum_attendees') 
            )
            db_session = db_connection.get_session()
            db_session.add(event)
            db_session.commit()

            return eventsInfo
