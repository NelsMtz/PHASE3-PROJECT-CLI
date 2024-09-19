# PHASE 3 PROJECT

## AUTHOR : NELLY MATU

## DATE 19TH SEP 2024

### OVERVIEW
For this phase 3 project, you will create a CLI and ORM application in Python. The major learning goals of project include;

- A CLI application that solves a real-world problem and adheres to best practices.
- A database created and modified with SQLAlchemy ORM with 3+ related tables.
- A well-maintained virtual environment using Pipenv.
- Proper package structure in your application.
- Use of lists, dicts, and tuples.


### Instructions:
- For this assignment, we'll be working on a project

- We have three tables: Buyers(name and email), products (name and price), and Orders(buyers_id, products_id, order_date)

- In this code, the relationship between buyers and orders is one-to-many (a buyer can have many orders), and the relationship between products and orders is also one-to-many (a product can have many orders). The relationship between buyers and products is many-to-many, with orders acting as a bridge table.

- Note: You should sketch your domain on paper or on a whiteboard before starting to code.

- Important: You will not be using SQLAlchemy for this challenge. - - Instead, use raw SQL queries. Write SQL queries directly in your - Python methods to perform the necessary operations on the database.


## DATABASE STRUCTURE
The database consists of three tables: buyers, products, and orders.

**Buyers Table**

id: A unique integer primary key for each buyer.
name: The name of the buyer.
email: The email address of the buyer.
orders: A relationship with the orders table, representing the orders made by each buyer.

**Products Table**

id: A unique integer primary key for each product.
name: The name of the product.
price: The price of the product.
orders: A relationship with the orders table, representing the orders that include each product.

**Orders Table**
id: A unique integer primary key for each order.
buyer_id: A foreign key referencing the id column of the buyers table, representing the buyer who made the order.
product_id: A foreign key referencing the id column of the products table, representing the product included in the order.
order_date: The date the order was made.

### DATABASE OPERATIONS
-- The code provides a Database class that allows you to perform the following operations:

- Create a new buyer
- Create a new product
- Create a new order
- Add an order to a buyer
- Add an order to a product
- Retrieve a buyer by ID
- Retrieve a product by ID
- Retrieve an order by ID
- Retrieve all buyers
- Retrieve all products
- Retrieve all orders

## MAIN FUNCTIONALITY
- The main function provides a command-line interface to interact with the database. You can create buyers, products, and orders, and view all existing data in the database.

### USAGE
To use the code, simply run the main function. You will be presented with a menu to choose from:

- Create buyer
- Create product
- Create order
- Add order to buyer
- Add order to product
- View all buyers
- View all products
- View all orders
- Exit

**Follow the prompts to perform the desired operation.**

### IMPLEMENTATION DETAILS
The code is implemented using Python and SQLAlchemy. The database model is defined using SQLAlchemy's declarative syntax, which allows for a clear and concise definition of the database structure.


## INSTALLATION
- To use this follow these steps:

### Alternative One
1.Open your terminal/cli on your computer. 
2.Clone the repository by running the following command:

 git clone https://github.com/NelsMtz/PHASE3-PROJECT-CLI.git

3.Change directory to the repo folder

    cd PHASE-3PROJECT-CLI
4.Open it in your Code Editor of choice. If you use VS Code, run the command:

    code .

### Alternative Two
1.On the top right corner of this page there is a button labelled Fork.

2.Click on that button to create a copy of the repository to your own account.

3.Follow the process described in Alternative One above.

4.Remember to replace your username when cloning.

    git clone https://github.com/NelsMtz/PHASE3-PROJECT-CLI.git

### Getting the files
*fork the repo Create a new branch in your terminal Install the prerequisite. Make appropriate changes in files. Run the server to see the changes Add the changes and commit them Push to the branch Create a pull request

Open the folder location on the terminal

### HOW TO RUN ALL CODES
clone the repository run from terminal

### DEPENDENCIES
practice python,SQL

### TECHNOLOGIES USED
Python,  OOP,SQL

  ## CONTACT INFO
.Email nmatu308@gmail.com

## LICENSE
MIT License Copyright (c) 2024 Nelly Matu