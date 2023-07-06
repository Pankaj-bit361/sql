# Problem: Create a Customers table / collection with the following fields: id (unique identifier), name, email, address, and phone_number.


# CREATE TABLE Customers (
#     id INT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100),
#     address VARCHAR(255),
#     phone_number VARCHAR(50)
# );


# Insert five rows / documents into the Customers table / collection with data of your choice.


# INSERT INTO Customers (id, name, email, address, phone_number)
# VALUES
#     (1, 'John Doe', 'john@example.com', '123 Main St', '123-456-7890'),
#     (2, 'Jane Smith', 'jane@example.com', '456 Elm St', '987-654-3210'),
#     (3, 'Bob Johnson', 'bob@example.com', '789 Oak St', '555-123-4567'),
#     (4, 'Alice Williams', 'alice@example.com', '321 Pine St', '444-888-9999'),
#     (5, 'Charlie Brown', 'charlie@example.com', '678 Maple St', '222-333-4444');



# Problem: Write a query to fetch all data from the Customers table / collection.

# SELECT * FROM Customers;

# Problem: Write a query to select only the name and email fields for all customers.

# SELECT name, email FROM Customers;


# Problem: Write a query to fetch the customer with the id of 3.

# SELECT * FROM Customers WHERE id = 3;

# Problem: Write a query to fetch all customers whose name starts with 'A'.

# SELECT * FROM Customers WHERE name LIKE 'A%';

# Problem: Write a query to fetch all customers, ordered by name in descending order.
# SELECT * FROM Customers ORDER BY name DESC;

# Problem: Write a query to update the address of the customer with id 4.

# UPDATE Customers SET address = 'New Address' WHERE id = 4;

# Problem: Write a query to fetch the top 3 customers when ordered by id in ascending order.
# SELECT * FROM Customers ORDER BY id ASC LIMIT 3;

# Problem: Write a query to delete the customer with id 2.

# DELETE FROM Customers WHERE id = 2;


# Problem: Write a query to count the number of customers.

# SELECT COUNT(*) AS total_customers FROM Customers;


# Problem: Write a query to count the number of customers.

# SELECT * FROM Customers ORDER BY id ASC OFFSET 2;

# Problem: Write a query to fetch all customers except the first two when ordered by id in ascending order.

# SELECT * FROM Customers ORDER BY id ASC OFFSET 2;

# Problem: Write a query to fetch all customers whose id is greater than 2 and name starts with 'B'.

# SELECT * FROM Customers WHERE id > 2 AND name LIKE 'B%';

# Problem: Write a query to fetch all customers whose id is less than 3 or name ends with 's'.

# SELECT * FROM Customers WHERE id < 3 OR name LIKE '%s';

# Problem: Write a query to fetch all customers where the phone_number field is not set or is null.

# SELECT * FROM Customers WHERE phone_number IS NULL OR phone_number = '';




