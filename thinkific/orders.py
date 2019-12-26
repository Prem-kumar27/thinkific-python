from .client import Client


class Orders:
    def __init__(self, client):
        self.__client = client

    def list(self, page: int = None, limit: int = None):
        return self.__client.request('get', '/orders', params={
            "page": page,
            "limit": limit
        })

    def retrieve_order(self, id: int):
        return self.__client.request('get', '/orders/%s' % id)
