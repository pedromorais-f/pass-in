from src.models.settings.connection import connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from src.errors.errors_types.http_conflict import HttpConflict


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
                raise HttpConflict('Check in already signed up')

            #General exception to return the database to a safe record
            except Exception as exception:
                session.rollback()
                raise exception