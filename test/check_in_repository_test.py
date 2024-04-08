import pytest
from src.models.settings.connection import connection_handler
from src.models.repository.check_ins_repository import CheckInsRepository

#Making the connection with database
connection_handler.connect_to_db()

@pytest.mark.skip(reason="Test Passed!")
def test_insert_check_in():
    check_in_attendee_id_key = "bbbbbbb-bbbbbb-bbbbbb-bbbbbbbb"

    check_ins_repository = CheckInsRepository()
    response = check_ins_repository.insert_check_in(check_in_attendee_id_key)
    print(response)