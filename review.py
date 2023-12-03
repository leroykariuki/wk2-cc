# review.py
from database import Database

db = Database('yelp.db')

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.id = db.insert_review(customer.id, restaurant.id, rating)
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant