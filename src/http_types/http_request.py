from typing import Dict

#Creating a class to http requests
class HttpRequest:
    def __init__(self, body: Dict = None, param: Dict = None) -> None:
        self.__body = body
        self.__param = param

    @property
    def get_body(self):
        return self.__body
        
    @property
    def get_param(self):
        return self.__param