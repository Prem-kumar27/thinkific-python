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

    def request(self, method=None, url=None, data=None, params=None):
        if data:
            data = json.dumps(data)
        result = requests.request(method=method, url=mergeURL(
            BASE_URL+url, params), data=data, headers=self.__headers)
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
