from typing import Dict, List
from src.models.settings.connection import connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.errors.errors_types.http_conflict import HttpConflict
from src.errors.errors_types.http_not_found import HttpNotFound

#Class that will make actions in the database
class AttendeesRepository:
    
    #Method to insert an Attendee in the database
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
            #Create a exception if the attendee already had been signed up
            except IntegrityError:
                raise HttpConflict('Attendee already signed up')

            #General exception to return the database to a safe record
            except Exception as exception:
                session.rollback()
                raise exception
        
    def get_attendee_by_id(self, attendee_id: str) -> Attendees:
        #Creating a query to get an attendee by the foreign key which is the id of the event
        with connection_handler as db_connection:
            try:
                session = db_connection.get_session

                attendee = (session.query(Attendees)
                            .join(Events, Events.id == Attendees.event_id)
                            .filter(Attendees.id == attendee_id)
                            .with_entities(Attendees.name, Attendees.id, Events.title)
                            .one()
                            )

                return attendee
            #Exception in case that attendee Id had not been found
            except NoResultFound:
                raise HttpNotFound('The attendee was not found!')
            
    def get_attendees_by_event_id(self, event_id: str) -> List[Dict]:
        #Creating a query to get attendees by the foreign key which is the id of the event
        with connection_handler as db_connection:
            session = db_connection.get_session

            #Using outerjoin method to return all the attendees
            attendees = (session.query(Attendees)
                        .outerjoin(CheckIns, CheckIns.attendeeId == Attendees.id)
                        .filter(Attendees.event_id == event_id)
                        .with_entities(Attendees.id, Attendees.name, Attendees.email, CheckIns.created_at.label('checked_in_at'))
                        .all()             
            )

            formatted_attendees = []
            for attendee in attendees:
                formatted_attendees.append(
                    {
                        "id": attendee.id,
                        "name": attendee.name,
                        "email": attendee.email,
                        "check_in_at": attendee.checked_in_at
                    }
                )
            if len(formatted_attendees) == 0: 
                raise HttpConflict('The event do not exist')
            
            return formatted_attendees

