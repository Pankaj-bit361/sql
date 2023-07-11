#  schema {
#   "_id": ObjectId(),
#   "driver_id": ObjectId(),
#   "passenger_id": ObjectId(),
#   "start_location": String,
#   "end_location": String,
#   "distance": Number,
#   "ride_time": Number,
#   "fare": Number
# }




# **Problem 26:**

# - **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
# - **Problem**: Create a **`Rides`** table / collection with the fields defined above.

# CREATE TABLE Rides (
#     id INT PRIMARY KEY,
#     driver_id INT,
#     passenger_id INT,
#     start_location VARCHAR(255),
#     end_location VARCHAR(255),
#     distance DECIMAL(10,2),
#     ride_time INT,
#     fare DECIMAL(10,2)
# );




# **Problem 27:**

# - **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
# - **Problem**: Insert five rows / documents into the **`Rides`** table / collection with data of your choice.

# INSERT INTO Rides (id, driver_id, passenger_id, start_location, end_location, distance, ride_time, fare)
# VALUES
#     (1, 101, 201, 'Location A', 'Location B', 10.5, 30, 15.50),
#     (2, 102, 202, 'Location C', 'Location D', 8.2, 25, 12.80),
#     (3, 103, 203, 'Location E', 'Location F', 15.3, 40, 20.75),
#     (4, 104, 204, 'Location G', 'Location H', 5.8, 15, 8.90),
#     (5, 105, 205, 'Location I', 'Location J', 12.1, 35, 18.20);




# **Problem 28:**

# - **Prerequisite**: Understand how to order data in SQL / MongoDB
# - **Problem**: Write a query to fetch all rides, ordered by **`fare`** in descending order.

# SELECT * FROM Rides ORDER BY fare DESC;






# **Problem 29:**

# - **Prerequisite**: Understand using math operations in SQL / MongoDB
# - **Problem**: Write a query to calculate the total **`distance`** and total **`fare`** for all rides.

# SELECT SUM(distance) AS total_distance, SUM(fare) AS total_fare FROM Rides;





# **Problem 30:**

# - **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
# - **Problem**: Write a query to calculate the average **`ride_time`** of all rides.

# SELECT AVG(ride_time) AS average_ride_time FROM Rides;






# **Problem 31:**

# - **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
# - **Problem**: Write a query to fetch all rides whose **`start_location`** or **`end_location`** contains 'Downtown'.

# SELECT * FROM Rides WHERE start_location LIKE '%Downtown%' OR end_location LIKE '%Downtown%';






# **Problem 32:**

# - **Prerequisite**: Understand how to use the COUNT function in SQL / MongoDB's aggregate functions
# - **Problem**: Write a query to count the number of rides for a given **`driver_id`**.

# SELECT COUNT(*) AS ride_count FROM Rides WHERE driver_id = <driver_id>;






# **Problem 33:**

# - **Prerequisite**: Understand data updating in SQL / MongoDB
# - **Problem**: Write a query to update the **`fare`** of the ride with **`id`** 4.

# UPDATE Rides SET fare = <new_fare> WHERE id = 4;






# **Problem 34:**

# - **Prerequisite**: Understand using GROUP BY in SQL / MongoDB's aggregate functions
# - **Problem**: Write a query to calculate the total **`fare`** for each **`driver_id`**.

# SELECT driver_id, SUM(fare) AS total_fare FROM Rides GROUP BY driver_id;







# **Problem 35:**

# - **Prerequisite**: Understand data deletion in SQL / MongoDB
# - **Problem**: Write a query to delete the ride with **`id`** 2. 

# DELETE FROM Rides WHERE id = 2;
