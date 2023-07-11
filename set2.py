# **Problem 16:**

# - **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
# - **Problem**: Create a **`Restaurants`** table / collection with the fields defined above.

# CREATE TABLE Restaurants (
#     id INT PRIMARY KEY,
#     name VARCHAR(100),
#     cuisine_type VARCHAR(100),
#     location VARCHAR(255),
#     average_rating DECIMAL(3,2),
#     delivery_available BOOLEAN
# );


# **Problem 17:**

# - **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
# - **Problem**: Insert five rows / documents into the **`Restaurants`** table / collection with data of your choice.


# INSERT INTO Restaurants (id, name, cuisine_type, location, average_rating, delivery_available)
# VALUES
#     (1, 'Restaurant 1', 'Italian', 'New York', 4.5, true),
#     (2, 'Restaurant 2', 'Mexican', 'Los Angeles', 4.2, false),
#     (3, 'Restaurant 3', 'Indian', 'London', 4.8, true),
#     (4, 'Restaurant 4', 'Chinese', 'Beijing', 3.9, true),
#     (5, 'Restaurant 5', 'Japanese', 'Tokyo', 4.6, false);



# **Problem 18:**

# - **Prerequisite**: Understand how to order data in SQL / MongoDB
# - **Problem**: Write a query to fetch all restaurants, ordered by **`average_rating`** in descending order.

# Ans-> SELECT * FROM Restaurants ORDER BY average_rating DESC;


# **Problem 19:**

# - **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
# - **Problem**: Write a query to fetch all restaurants that offer **`delivery_available`** and have an **`average_rating`** of more than 4.

# SELECT * FROM Restaurants WHERE delivery_available = true AND average_rating > 4;





# **Problem 20:**

# - **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
# - **Problem**: Write a query to fetch all restaurants where the **`cuisine_type`** field is not set or is null.

# SELECT * FROM Restaurants WHERE cuisine_type IS NULL;




# **Problem 21:**

# - **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
# - **Problem**: Write a query to count the number of restaurants that have **`delivery_available`**.


# Ans-> SELECT COUNT(*) FROM Restaurants WHERE delivery_available = true;





# **Problem 22:**

# - **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
# - **Problem**: Write a query to fetch all restaurants whose **`location`** contains 'New York'.

# SELECT * FROM Restaurants WHERE location LIKE '%New York%';







# **Problem 23:**

# - **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
# - **Problem**: Write a query to calculate the average **`average_rating`** of all restaurants.

# SELECT AVG(average_rating) AS average_rating FROM Restaurants;







# **Problem 24:**

# - **Prerequisite**: Understand how to limit results in SQL / MongoDB
# - **Problem**: Write a query to fetch the top 5 restaurants when ordered by **`average_rating`** in descending order.


# SELECT * FROM Restaurants ORDER BY average_rating DESC LIMIT 5;






# **Problem 25:**

# - **Prerequisite**: Understand data deletion in SQL / MongoDB
# - **Problem**: Write a query to delete the restaurant with **`id`** 3.

# DELETE FROM Restaurants WHERE id = 3;
