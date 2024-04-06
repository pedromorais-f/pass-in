from src.models.settings.connection import connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError, NoResultFound


#Class that will make actions in the database
class CheckInsRepository:
    
    #Method to insert a Attendee in the database
    def insert_check_in(self, attendee_id_info:str) -> str:
        #Creating the insertion of the Check In
        with connection_handler as db_connection:
            try:
                check_in = CheckIns(
                    attendeeId = attendee_id_info
                )
                session = db_connection.get_session
                session.add(check_in)
                session.commit()

                return attendee_id_info
            #Create a exception if the check in already had been signed up
            except IntegrityError:
                raise Exception('Check in already signed up')

            #General exception to return the database to a safe record
            except Exception as exception:
                session.rollback()
                raise exception
            
    def get_check_in_by_id(self, attendee_id_info: str) -> CheckIns:
        #Creating a query to get a check in by the foreign key which is attendee id 
        with connection_handler as db_connection:
            try:
                session = db_connection.get_session

                check_in = (session.query(CheckIns)
                            .join(Attendees, Attendees.id == CheckIns.attendeeId)
                            .join(Events, Events.id == Attendees.event_id)
                            .filter(CheckIns.attendeeId == attendee_id_info)
                            .with_entities(CheckIns.attendeeId, Attendees.name, Attendees.email, Events.title)
                            .one()
                            )

                return check_in
            #Exception in case that attendee Id had not been found
            except NoResultFound:
                return None