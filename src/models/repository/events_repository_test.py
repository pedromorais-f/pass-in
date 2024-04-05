from src.models.settings.connection import connection_handler
from .events_repository import EventsRepository

#Making the connection with database
connection_handler.connect_to_db()

def insert_event_test():
    event = {
        'uuid': 'dhfgiujhgf-d3432d34443-d34442343dfsIKF',
        'title': 'Insert Event Test',
        'details': 'Testing the Event Repository',
        'slug': 'insert-event-test',
        'maximum_attendees': 100
    }

    event_repository = EventsRepository()
    response = event_repository.insert_event(event)
    print(response)

insert_event_test()