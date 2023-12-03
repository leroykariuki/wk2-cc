# main.py
from restaurant import Restaurant
from review import Review
from customer import Customer

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

def add_review():
    print("\nEnter Review Details:")
    given_name = input("Customer Given Name: ")
    family_name = input("Customer Family Name: ")
    restaurant_name = input("Restaurant Name: ")
    rating = int(input("Rating (1-5): "))

    customer = Customer(given_name, family_name)
    restaurant = Restaurant(restaurant_name)
    review = Review(customer, restaurant, rating)

    print("Review added successfully!")

def get_reviews_for_restaurant():
    restaurant_name = input("Enter Restaurant Name: ")
    restaurant = next((r for r in Restaurant.all_restaurants if r.get_name() == restaurant_name), None)

    if restaurant:
        print(f"\nReviews for {restaurant.get_name()}:")
        for review in restaurant.get_reviews():
            print(f"Rating: {review.get_rating()} by {review.get_customer().full_name()}")
    else:
        print("Restaurant not found.")

def get_customers_for_restaurant():
    restaurant_name = input("Enter Restaurant Name: ")
    restaurant = next((r for r in Restaurant.all_restaurants if r.get_name() == restaurant_name), None)

    if restaurant:
        customers = list(set([review.get_customer().full_name() for review in restaurant.get_reviews()]))
        print(f"\nCustomers who reviewed {restaurant.get_name()}: {', '.join(customers)}")
    else:
        print("Restaurant not found.")

def get_restaurants_for_customer():
    customer_name = input("Enter Customer Full Name: ")
    customer = next((c for c in Customer.all_customers if c.full_name() == customer_name), None)

    if customer:
        restaurants = list(set([review.get_restaurant().get_name() for review in customer.reviews]))
        print(f"\nRestaurants reviewed by {customer.full_name()}: {', '.join(restaurants)}")
    else:
        print("Customer not found.")

def get_num_reviews_for_customer():
    customer_name = input("Enter Customer Full Name: ")
    customer = next((c for c in Customer.all_customers if c.full_name() == customer_name), None)

    if customer:
        print(f"\n{customer.full_name()} has authored {customer.num_reviews()} reviews.")
    else:
        print("Customer not found.")

def find_customer_by_name():
    full_name = input("Enter Customer Full Name: ")
    customer = Customer.find_by_name(full_name)

    if customer:
        print(f"\nFound Customer: {customer.full_name()}")
    else:
        print("Customer not found.")

def find_all_customers_by_given_name():
    given_name = input("Enter Customer Given Name: ")
    customers = Customer.find_all_by_given_name(given_name)

    if customers:
        names = [customer.full_name() for customer in customers]
        print(f"\nCustomers with the given name '{given_name}': {', '.join(names)}")
    else:
        print("No customers found with the given name.")

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_review()
        elif choice == "2":
            get_reviews_for_restaurant()
        elif choice == "3":
            get_customers_for_restaurant()
        elif choice == "4":
            get_restaurants_for_customer()
        elif choice == "5":
            get_num_reviews_for_customer()
        elif choice == "6":
            find_customer_by_name()
        elif choice == "7":
            find_all_customers_by_given_name()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")