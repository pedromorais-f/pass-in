from typing import Dict

class HttpResponse:
    def __init__(self, body: Dict, status_code: int) -> None:
        self.__body = body
        self.__status_code = status_code
        