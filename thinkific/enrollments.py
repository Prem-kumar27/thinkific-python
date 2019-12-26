from .client import Client

class Enrollments:
    def __init__(self, client):
        self.__client = client

    def list(self, page: int = None, limit: int = None, 
            user_id: int = None, course_id: int = None, email: str = None,
            free_trial: bool = None, full: bool= None, completed: bool = None,
            expired: bool = None, created_on: str = None, created_before: str = None,
            created_on_or_before: str = None, created_after: str = None, created_on_or_after: str = None,
            updated_on: str = None,updated_before: str = None, updated_on_or_before: str = None,updated_after: str=None):
        params = {
            "page": page,
            "limit": limit,
            "query[user_id]": user_id,
            "query[course_id]": course_id ,
            "query[email]": email,
            "query[free_trial]": free_trial,
            "query[full]": full,
            "query[completed]": completed ,
            "query[expired]": expired,
            "query[created_on]": created_on ,
            "query[created_before]": created_before,
            "query[created_on_or_before]":created_on_or_before ,
            "query[created_after]": created_after,
            "query[created_on_or_after]":created_on_or_after ,
            "query[updated_on]": updated_on,
            "query[updated_before]": updated_before,
            "query[updated_on_or_before]":updated_on_or_before ,
            "query[updated_after]": updated_after,
        }
        return self.__client.request('get','/enrollments',params=params)
    
    def retrieve_enrollment(self, id: int ):
        return self.__client.request('get','/enrollments/%s' %id)

    def create_enrollment(self, values: dict):
        return self.__client.request('post','/enrollments', data=values)
    
    def update_enrollment(self,id: int, values: dict):
        return self.__client.request('put','/enrollments/%s' %id, data=values)