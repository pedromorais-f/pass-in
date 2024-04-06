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
    attendee_id = 'bbbbbbb-bbbbbb-bbbbbb-bbbbbbbb1'
    
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_by_id(attendee_id)
    print(response)