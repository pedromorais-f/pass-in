from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.errors.errors_types.http_conflict import HttpConflict
from src.errors.errors_types.http_not_found import HttpNotFound

#Class to handle with registry of attendees in some event
class AttendeeHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    #Method to register an attendee
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.get_body
        event_id = http_request.get_param["event_id"]
        try:
            event = self.__events_repository.get_event_by_id(event_id)
        except Exception:
            raise HttpNotFound('This event not exist!')
        
        body['uuid'] = str(uuid.uuid4())



        event_counter = self.__events_repository.count_event_attendees(event_id)
        if(event_counter['maximumAttendees'] != 0 and event_counter['maximumAttendees'] == event_counter['attendeesAmount']):
            raise HttpConflict('Sold Out')
        
        body['event_id'] = event_id
        self.__attendees_repository.insert_attendee(body)

        return HttpResponse(body={'attendee_id': body['uuid'], 'event_title': event.title }, status_code=201)
    
    #Method to find a attendee badge in the database
    def find_attendee_badge(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.get_param["attendee_id"]

        try:
            badge = self.__attendees_repository.get_attendee_by_id(attendee_id)

            return HttpResponse(body={
                'badge': {
                    "name": badge.name,
                    "attendee_id": badge.id,
                    "event": badge.title
                }
            }, status_code=200)
        except Exception:
            raise HttpNotFound('The attendee was not found!')
        
    #Method to list all the attendees in a event
    def find_attnedees_from_event(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.get_param["event_id"]
        try:
            attendees = self.__attendees_repository.get_attendees_by_event_id(event_id)

            return HttpResponse(body={"attendees": attendees}, status_code=200)
        except Exception:
            raise HttpNotFound('This event do not have attendees')


