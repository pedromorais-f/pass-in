import pytest
from src.models.settings.connection import connection_handler
from src.models.repository.attendees_repository import AttendeesRepository

#Making the connection with database
connection_handler.connect_to_db()

@pytest.mark.skip(reason="Test Passed!")
def test_insert_attendee():
    event_id_key = "dhfgiujhgf-d3432d34443-d34442343dfsIKF"
    attendee = {
        'uuid': 'bbbbbbb-bbbbbb-bbbbbb-bbbbbbbb',
        'name': 'AttendeeY',
        'email': 'attendeeY@email.com',
        'event_id': event_id_key
    }

    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendee)
    print(response)

@pytest.mark.skip(reason="Test Passed!")
def test_get_attendee_by_id():
    attendee_id = 'f1ef1be9-8dfd-4f3b-83b9-94ecf43a8fbc'
    
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_by_id(attendee_id)
    print(response)

@pytest.mark.skip(reason="Test Passed!")
def test_get_attendees_by_event_id():
    event_id = '9a938ca7-c428-4a51-8ebc-9a871dd2c0721'
    
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendees_by_event_id(event_id)
    for item in response:
        print(item)