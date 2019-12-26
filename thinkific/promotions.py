from .client import Client

class Promotions:
    def __init__(self, client):
        self.__client = client
    
    def list(self, page: int = None, limit: int = None):
        return self.__client.request('get','/promotions',params={
            "page": page,
            "limit": limit
        })
    
    def retrieve_promotion(self, id: int):
        return self.__client.request('get','/promotions/%s' %id)
    
    def create_promotion(self, values: dict):
        return self.__client.request('post','/promotions', data=
            values
        )

    def update_promotion(self, id: int, values: dict):
        return self.__client.request('put','/promotions/%s' %id, data=
            values
        ) 
    
    def delete_promotion(self, id: int):
        return self.__client.request('delete','/promotions/%s' %id) 

    def find_promotion_with_coupon_and_product(self, product_id: int, coupon_code: int):
        return self.__client.request('get','/promotions/by_coupon', params={
            "product_id": product_id,
            "coupon_code": coupon_code
        })
