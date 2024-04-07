from typing import Dict

#Creating a class to http responses
class HttpResponse:
    def __init__(self, body: Dict, status_code: int) -> None:
        self.__body = body
        self.__status_code = status_code

    @property
    def get_body(self):
        return self.__body
        
    @property
    def get_status_code(self):
        return self.__status_code
        