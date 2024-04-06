from typing import Dict
from src.models.settings.connection import connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError, NoResultFound

#Class that will make actions in the database
class AttendeesRepository:
    
    #Method to insert a Attendee in the database
    def insert_attendee(self, attendees_info:Dict) -> Dict:
        #Creating the insertion of the Attendee
        with connection_handler as db_connection:
            try:
                attendee = Attendees(
                    id = attendees_info.get('uuid'),
                    name = attendees_info.get('name'),
                    email = attendees_info.get('email'),
                    event_id = attendees_info.get('event_id'), 
                )
                session = db_connection.get_session
                session.add(attendee)
                session.commit()

                return attendees_info
            except IntegrityError:
                raise Exception('Attendee already signed up')

            except Exception as exception:
                session.rollback()
                raise exception
        
    def get_attendee_by_id(self, attendee_id: str) -> Attendees:
        #Creating a query to get a attendee by the primary key which is the id of the event
        with connection_handler as db_connection:
            try:
                session = db_connection.get_session

                attendee = (session.query(Attendees)
                            .join(Events, Events.id == Attendees.event_id)
                            .filter(Attendees.id == attendee_id)
                            .with_entities(Attendees.name, Attendees.email, Events.title)
                            .one()
                            )

                return attendee
            except NoResultFound:
                return None

