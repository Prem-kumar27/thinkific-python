from .client import Client


class CourseReviews:
    def __init__(self, client):
        self.__client = client

    def list(self, course_id: int, page: int = None,
             limit: int = None, approved: bool = None):
        return self.__client.request('get', '/course_reviews', params={
            "course_id": course_id,
            "page": page,
            "limit": limit,
            "approved": approved
        })

    def create_course_review(self, course_id: int, values: dict):
        return self.__client.request('post', '/course_reviews', params={
            "course_id": course_id
        },
            data=values)

    def retrieve_course_review(self, course_id: int):
        return self.__client.request('put', '/course_reviews/%s' % course_id)
