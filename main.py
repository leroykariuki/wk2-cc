# main.py
from restaurant import Restaurant
from review import Review
from customer import Customer
from database import Database  # Import the Database class

def print_menu():
    print("\nMenu:")
    print("1. Add a Review")
    print("2. Get Reviews for a Restaurant")
    print("3. Get Customers who Reviewed a Restaurant")
    print("4. Get Restaurants Reviewed by a Customer")
    print("5. Get Number of Reviews by a Customer")
    print("6. Find Customer by Full Name")
    print("7. Find All Customers by Given Name")
    print("8. Exit")

def add_review(db):
    print("\nEnter Review Details:")
    given_name = input("Customer Given Name: ")
    family_name = input("Customer Family Name: ")
    restaurant_name = input("Restaurant Name: ")
    rating = int(input("Rating (1-5): "))

    customer = Customer(given_name, family_name)
    restaurant = Restaurant(restaurant_name)
    review = Review(customer, restaurant, rating)

    # Save data to the database
    db.insert_review(customer.id, restaurant.id, rating)

    print("Review added successfully!")

def get_reviews_for_restaurant(db):
    restaurant_name = input("Enter Restaurant Name: ")
    restaurant = next((r for r in Restaurant.all_restaurants if r.get_name() == restaurant_name), None)

    if restaurant:
        print(f"\nReviews for {restaurant.get_name()}:")
        reviews = db.get_restaurant_reviews(restaurant.id)
        for review_data in reviews:
            customer_id, rating = review_data[1], review_data[3]
            customer = next((c for c in Customer.all_customers if c.id == customer_id), None)
            if customer:
                print(f"Rating: {rating} by {customer.full_name()}")
    else:
        print("Restaurant not found.")

def get_customers_for_restaurant(db):
    restaurant_name = input("Enter Restaurant Name: ")
    restaurant = next((r for r in Restaurant.all_restaurants if r.get_name() == restaurant_name), None)

    if restaurant:
        print(f"\nCustomers who reviewed {restaurant.get_name()}:")
        reviews = db.get_restaurant_reviews(restaurant.id)
        for review_data in reviews:
            customer_id = review_data[1]
            customer = next((c for c in Customer.all_customers if c.id == customer_id), None)
            if customer:
                print(f"{customer.full_name()}")
    else:
        print("Restaurant not found.")

def get_restaurants_for_customer(db):
    given_name = input("Enter Customer's Given Name: ")
    customers = db.find_all_customers_by_given_name(given_name)

    if customers:
        customer = customers[0]  # Assuming the first customer with the given name
        print(f"\nRestaurants reviewed by {customer.full_name()}:")
        for restaurant in customer.restaurants():
            print(restaurant.get_name())
    else:
        print("Customer not found.")

def get_num_reviews_for_customer(db):
    given_name = input("Enter Customer's Given Name: ")
    customers = db.find_all_customers_by_given_name(given_name)

    if customers:
        customer = customers[0]  # Assuming the first customer with the given name
        print(f"\nNumber of reviews by {customer.full_name()}: {customer.num_reviews()}")
    else:
        print("Customer not found.")

def find_customer_by_full_name(db):
    full_name = input("Enter Customer's Full Name: ")
    customer = db.find_customer_by_name(full_name)

    if customer:
        print(f"\nCustomer found: {customer.full_name()}")
    else:
        print("Customer not found.")

def find_all_customers_by_given_name(db):
    given_name = input("Enter Customer's Given Name: ")
    customers = db.find_all_customers_by_given_name(given_name)

    if customers:
        print(f"\nCustomers with given name {given_name}:")
        for customer in customers:
            print(customer.full_name())
    else:
        print("No customers found with the given name.")

if __name__ == "__main__":
    db = Database('yelp.db')  # Create the database instance
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_review(db)
        elif choice == "2":
            get_reviews_for_restaurant(db)
        elif choice == "3":
            get_customers_for_restaurant(db)
        elif choice == "4":
            get_restaurants_for_customer(db)
        elif choice == "5":
            get_num_reviews_for_customer(db)
        elif choice == "6":
            find_customer_by_full_name(db)
        elif choice == "7":
            find_all_customers_by_given_name(db)
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
