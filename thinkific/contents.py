from .client import Client

class Contents:
    def __init__(self, client):
        self.__client = client

    def retrieve_content(self, id: int):
        return self.__client.request('get','/contents/%s' %id)

