import pytest
from src.models.settings.connection import connection_handler
from src.models.repository.events_repository import EventsRepository

#Making the connection with database
connection_handler.connect_to_db()

@pytest.mark.skip(reason="Test Passed!")
def test_insert_event():
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


@pytest.mark.skip(reason="Test Passed!")
def test_get_event_by_id():
    event_id = 'dhfgiujhgf-d3432d34443-d34442343dfsIKF12'
    
    event_repository = EventsRepository()
    response = event_repository.get_event_by_id(event_id)
    print(response)