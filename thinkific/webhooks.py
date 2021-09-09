from .client import Client


class Webhooks:
    def __init__(self, client):
        self.__client = client

    def list(self, page: int = None, limit: int = None):
        params = {
            "page": page,
            "limit": limit
        }
        return self.__client.request('get', '/webhooks', params=params, api='Webhooks')

    def create_webhook(self, values: dict):
        return self.__client.request('post', '/webhooks', data=values, api='Webhooks')

    def retrieve_webhook(self, id: string):
        return self.__client.request('get', '/webhooks/%s' % id, api='Webhooks')

    def update_webhook(self, id: string, values: dict):
        return self.__client.request('put', '/webhooks/%s' % id, data=values, api='Webhooks')

    def delete_webhook(self, id: string):
        return self.__client.request('delete', '/webhooks/%s' % id, api='Webhooks')
