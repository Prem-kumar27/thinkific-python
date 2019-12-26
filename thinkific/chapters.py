from .client import Client


class Chapters:
    def __init__(self, client):
        self.__client = client

    def retrieve_chapter(self, id: int):
        return self.__client.request('get', '/chapters/%s' % id)

    def retrieve_contents_of_chapter(self, chapter_id: int, page: int = None, limit: int = None):
        return self.__client.request('get', '/chapters/%s/contents' % chapter_id, params={
            "page": page,
            "limit": limit
        })
