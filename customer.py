# customer.py
from database import Database

db = Database('yelp.db')

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        self.id = db.insert_customer(given_name, family_name)
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return list(set([review.get_restaurant() for review in self.reviews]))

    def add_review(self, restaurant, rating):
        from review import Review  # Importing here to avoid circular import
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]