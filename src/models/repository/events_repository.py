from typing import Dict
from src.models.settings.connection import connection_handler
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError, NoResultFound

#Class that will make actions in the database
class EventsRepository:
    
    #Method to insert a Event in the database
    def insert_event(self, events_info:Dict) -> Dict:
        #Creating the insertion of the Event
        with connection_handler as db_connection:
            try:
                event = Events(
                    id = events_info.get('uuid'),
                    title = events_info.get('title'),
                    details = events_info.get('details'),
                    slug = events_info.get('slug'),
                    maximum_attendees = events_info.get('maximum_attendees') 
                )
                session = db_connection.get_session
                session.add(event)
                session.commit()

                return events_info
            #Exception in case that event already had been signed up
            except IntegrityError:
                raise Exception('Event already signed up')

            #General exception that will return the database to the last state
            except Exception as exception:
                session.rollback()
                raise exception
        
    def get_event_by_id(self, event_id: str) -> Events:
        #Creating a query to get a event by the primary key which is the id
        with connection_handler as db_connection:
            try:
                session = db_connection.get_session

                event = session.query(Events).filter(Events.id == event_id).one()

                return event
            #Exceptioon in case the event id had not been found
            except NoResultFound:
                return None

