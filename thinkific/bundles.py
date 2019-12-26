from .client import Client


class Bundles:
    def __init__(self, client):
        self.__client = client

    def retrieve_bundle(self, id: int):
        return self.__client.request('get', '/bundles/%s' % id)

    def retrieve_courses_in_bundle(self, id: int, page: int = None,
                                   limit: int = None):
        return self.__client.request('get', 'bundles/%s/courses' % id, params={
            "page": page,
            "limit": limit
        })

    def create_enrollment_in_bundle(self, bundle_id: int, values: dict):
        return self.__client.request('post', '/bundles/%s/courses' % bundle_id, data=values)

    def get_enrollments_in_bundle(self, bundle_id: int, page: int = None,
                                  limit: int = None):
        return self.__client.request('get', 'bundles/%s/enrollments' % bundle_id, params={
            "page": page,
            "limit": limit
        })

    def update_enrollments_in_bundle(self, bundle_id: int, values: dict):
        return self.__client.request('put', 'bundles/%s/enrollments' % bundle_id, data=values)
