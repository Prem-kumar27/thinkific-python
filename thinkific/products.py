from .client import Client

class Products:
    def __init__(self, client):
        self.__client = client
    
    def list(self, page: int = None, limit: int = None):
        return self.__client.request('get','/products',params={
            "page": page,
            "limit": limit
        })
    
    def retrieve_product(self, id: int):
        return self.__client.request('get','/products/%s' %id)
    
    def retrieve_product_related(self, id:int, page: int = None, 
                                 limit: int = None ):
        return self.__client.request('get','products/%s/related' %id,params={
            "page": page,
            "limit": limit
        })


