from .client import Client


class Users:
    def __init__(self, client):
        self.__client = client

    def list(self, page: int = None, limit: int = None, email: str = None,
             role: str = None, external_source: str = None, custom_profile_field_label: str = None,
             custom_profile_field_value: str = None, group_id: str = None):
        params = {
            "page": page,
            "limit": limit,
            "query[email]": email,
            "query[role]": role,
            "query[external_source]": external_source,
            "query[custom_profile_field_label]": custom_profile_field_label,
            "query[custom_profile_field_value]": custom_profile_field_value,
            "query[group_id]": group_id
        }
        return self.__client.request('get', '/users', params=params)

    def retrieve_user(self, id: int):
        return self.__client.request('get', '/users/%s' % id)

    def create_user(self, values: dict):
        return self.__client.request('post', '/users', data=values
                                     )

    def update_user(self, id: int, values: dict):
        return self.__client.request('put', '/users/%s' % id, data=values
                                     )

    def delete_user(self, id: int):
        return self.__client.request('delete', '/users/%s' % id)
