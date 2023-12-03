# database.py
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS restaurants (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                given_name TEXT,
                family_name TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                restaurant_id INTEGER,
                rating INTEGER,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
            )
        ''')

        self.conn.commit()

    def insert_restaurant(self, name):
        self.cursor.execute("INSERT INTO restaurants (name) VALUES (?)", (name,))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_customer(self, given_name, family_name):
        self.cursor.execute("INSERT INTO customers (given_name, family_name) VALUES (?, ?)", (given_name, family_name))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_review(self, customer_id, restaurant_id, rating):
        self.cursor.execute("INSERT INTO reviews (customer_id, restaurant_id, rating) VALUES (?, ?, ?)",
                            (customer_id, restaurant_id, rating))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_restaurant_reviews(self, restaurant_id):
        self.cursor.execute("SELECT * FROM reviews WHERE restaurant_id = ?", (restaurant_id,))
        return self.cursor.fetchall()
    
    