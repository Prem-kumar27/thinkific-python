import json
import requests
from .utils import *


class Client(object):
    def __init__(self, api_key, subdomain, headers={}):
        self.__headers = {
            'X-Auth-API-Key': '%s' % api_key,
            'X-Auth-Subdomain': '%s' % subdomain,
            'Content-Type': 'application/json',
        }

        self.__headers_webhooks = {
            'Authorization: Bearer ': '%s' % api_key,
            'Content-Type': 'application/json'
        }

    def request(self, method=None, url=None, data=None, params=None, api='Admin'):
        if data:
            data = json.dumps(data)

        if api == 'Admin':
            full_url = mergeURL(BASE_URL + ADMIN_API_URL + url, params)
            result = requests.request(method=method, url=full_url, data=data, headers=self.__headers)
        elif api == 'Webhooks':
            full_url = mergeURL(BASE_URL + WEBHOOKS_API_URL + url, params)
            result = requests.request(method=method, url=full_url, data=data, headers=self.__headers_webhooks)
        else:
            return 'API provided is not available'

        return self.__validator(result)

    def __validator(self, result):
        try:
            body = json.loads(result.text)
        except Exception:
            body = {}
        if result.status_code >= 400:
            raise Exception(result.status_code)
        else:
            return body
