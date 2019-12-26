from .client import Client
from .users import Users
from .promotions import Promotions
from .enrollments import Enrollments
from .courses import Courses
from .coupons import Coupons
from .contents import Contents
from .products import Products
from .bundles import Bundles
from .course_reviews import CourseReviews


class Thinkific:
    def __init__(self, api_key, subdomain):
        client = Client(api_key, subdomain)
        self.__users = Users(client)
        self.__promotions = Promotions(client)
        self.__enrollments = Enrollments(client)
        self.__courses = Courses(client)
        self.__coupons = Coupons(client)
        self.__contents = Contents(client)
        self.__products = Products(client)
        self.__bundles = Bundles(client)
        self.__course_reviews = CourseReviews(client)

    @property
    def users(self):
        return self.__users

    @property
    def promotions(self):
        return self.__promotions

    @property
    def enrollments(self):
        return self.__enrollments

    @property
    def courses(self):
        return self.__courses

    @property
    def coupons(self):
        return self.__coupons

    @property
    def contents(self):
        return self.__contents

    @property
    def products(self):
        return self.__products

    @property
    def bundles(self):
        return self.__bundles

    @property
    def course_reviews(self):
        return self.__course_reviews
