from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
import uuid

#Class to handle with events requests and responses
class EventHandler:
    def __init__(self) -> None:
        self.__event_repository = EventsRepository()

    #Method to register a event in the database
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.get_body
        body['uuid'] = str(uuid.uuid4())
        self.__event_repository.insert_event(body)

        return HttpResponse(
            body={'event_id': body['uuid']},
            status_code= 200
        )
    
    #Method to find a event in database and return all the informations about it
    def find_event_by_id(self, http_request: HttpRequest) -> HttpResponse:
        try:
            event_id = http_request.get_param["event_id"]
            event = self.__event_repository.get_event_by_id(event_id)

            event_attendees_counter = self.__event_repository.count_event_attendees(event_id)

            return HttpResponse(body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.slug,
                    "maximum_attendees": event.maximum_attendees,
                    "attendeesAmount": event_attendees_counter["attendeesAmount"]
                }
            }, status_code= 201)
        except Exception:
            raise Exception('Event was not found')



