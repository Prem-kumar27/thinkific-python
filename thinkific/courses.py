from .client import Client

class Courses:
    def __init__(self, client):
        self.__client = client
    
    def list(self, page: int = None, limit: int = None):
        return self.__client.request('get','/courses',params={
            "page": page,
            "limit": limit
        })
    
    def retrieve_course(self, id: int):
        return self.__client.request('get','/courses/%s' %id)

    def retrieve_chapters(self, course_id: int):
        return self.__client.request('get','/courses/%s/chapters' %course_id)