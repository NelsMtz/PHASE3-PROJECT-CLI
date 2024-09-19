from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Buyer(Base):
    __tablename__ = 'buyers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    orders = relationship('Order', backref='buyer')

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    orders = relationship('Order', backref='product')

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, ForeignKey('buyers.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    order_date = Column(String)

DATABASE_URL = "sqlite:///buyers.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)

class Database:
    def __init__(self):
        self.db = SessionLocal()

    def create_buyer(self, buyer):
        self.db.add(buyer)
        self.db.commit()
        self.db.refresh(buyer)

    def create_product(self, product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)

    def create_order(self, order):
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)

    def add_order_to_buyer(self, buyer, order):
        buyer.orders.append(order)
        self.db.commit()

    def add_order_to_product(self, product, order):
        product.orders.append(order)
        self.db.commit()

    def get_buyer(self, buyer_id):
        return self.db.query(Buyer).get(buyer_id)

    def get_product(self, product_id):
        return self.db.query(Product).get(product_id)

    def get_order(self, order_id):
        return self.db.query(Order).get(order_id)

    def get_all_buyers(self):
        return self.db.query(Buyer).all()

    def get_all_products(self):
        return self.db.query(Product).all()

    def get_all_orders(self):
        return self.db.query(Order).all()

def main():
    db = Database()

    while True:
        print("1. Create buyer")
        print("2. Create product")
        print("3. Create order")
        print("4. Add order to buyer")
        print("5. Add order to product")
        print("6. View all buyers")
        print("7. View all products")
        print("8. View all orders")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter buyer name: ")
            email = input("Enter buyer email: ")
            buyer = Buyer(name=name, email=email)
            db.create_buyer(buyer)
            print("Buyer created successfully!")
        elif choice == "2":
            name = input("Enter product name: ")
            price = int(input("Enter product price: "))
            product = Product(name=name, price=price)
            db.create_product(product)
            print("Product created successfully!")
        elif choice == "3":
            buyer_id = int(input("Enter buyer ID: "))
            product_id = int(input("Enter product ID: "))
            order_date = input("Enter order date: ")
            order = Order(buyer_id=buyer_id, product_id=product_id, order_date=order_date)
            db.create_order(order)
            print("Order created successfully!")
        elif choice == "4":
            buyer_id = int(input("Enter buyer ID: "))
            order_id = int(input("Enter order ID: "))
            buyer = db.get_buyer(buyer_id)
            order = db.get_order(order_id)
            if buyer and order:
                db.add_order_to_buyer(buyer, order)
                print("Order added to buyer successfully!")
            else:
                print("Invalid buyer or order ID.")
        elif choice == "5":
            product_id = int(input("Enter product ID: "))
            order_id = int(input("Enter order ID: "))
            product = db.get_product(product_id)
            order = db.get_order(order_id)
            if product and order:
                db.add_order_to_product(product, order)
                print("Order added to product successfully!")
            else:
                print("Invalid product or order ID.")
        elif choice == "6":
            buyers = db.get_all_buyers()
            for buyer in buyers:
                print(f"Buyer {buyer.id}: {buyer.name}, {buyer.email}")
            print("Total buyers:", len(buyers))
        elif choice == "7":
            products = db.get_all_products()
            for product in products:
                print(f"Product {product.id}: {product.name}, {product.price}")
            print("Total products:", len(products))
        elif choice == "8":
            orders = db.get_all_orders()
            for order in orders:
                print(f"Order {order.id}: Buyer {order.buyer_id}, Product {order.product_id}, {order.order_date}")
            print("Total orders:", len(orders))
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()