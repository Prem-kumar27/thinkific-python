from .client import Client


class Coupons:
    def __init__(self, client):
        self.__client = client

    def list(self, promotion_id: int, page: int = None, limit: int = None):
        return self.__client.request('get', '/coupons', params={
            "promotion_id": promotion_id,
            "page": page,
            "limit": limit
        })

    def retrieve_coupon(self, coupon_id: int):
        return self.__client.request('get', '/coupons/%s' % coupon_id)

    def create_coupon(self, promotion_id: int, values: dict):
        return self.__client.request('post', '/coupons', params={
            "promotion_id": promotion_id
        },
            data=values)

    def bulk_create_coupons(self, promotion_id: int, values: dict):
        return self.__client.request('post', '/coupons/bulk_create', params={
            "promotion_id": promotion_id},
            data=values)

    def update_coupon(self, coupon_id: int, values: dict):
        return self.__client.request('put', '/coupons/%s' % coupon_id, data=values)

    def delete_coupon(self, coupon_id: int):
        return self.__client.request('delete', '/coupons/%s' % coupon_id)
