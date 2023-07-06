from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to get a new connection and cursor
def get_db():
    conn = sqlite3.connect('database.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn, conn.cursor()

# Routes for your Flask application
@app.route("/")
def welcome():
    return "Welcome to home page"

@app.route("/addDish", methods=["POST"])
def adddish():
    if request.method == 'POST':
        data = request.get_json()
        conn, c = get_db()
        c.execute("INSERT INTO dish (Name, Quantity, Price, Img) VALUES (?, ?, ?, ?)",
                  (data['Name'], data['Quantity'], data['Price'], data['Img']))
        conn.commit()
        conn.close()
        return jsonify("Dish has been added successfully")

@app.route("/menu", methods=["GET"])
def showmenu():
    if request.method == "GET":
        conn, c = get_db()
        c.execute("SELECT * FROM dish")
        data = c.fetchall()
        result = []
        for item in data:
            result.append({
                'id': item[0],
                'Name': item[1],
                'Quantity': item[2],
                'Price': item[3],
                'Img': item[4]
            })
        conn.close()
        return jsonify(result)

@app.route("/delete/<int:Id>", methods=["DELETE"])
def deleteDish(Id):
    conn, c = get_db()
    c.execute("DELETE FROM dish WHERE id=?", (Id,))
    conn.commit()

    if c.rowcount > 0:
        conn.close()
        return jsonify("Dish has been removed successfully")

    conn.close()
    return jsonify("Dish not found")

@app.route("/updateDish/<int:id>", methods=["PATCH"])
def updateDish(id):
    if request.method == "PATCH":
        data = request.get_json()
        conn, c = get_db()
        c.execute("UPDATE dish SET Quantity=?, Name=?, Price=?, Img=? WHERE id=?",
                  (data['Quantity'], data['Name'], data['Price'], data['Img'], id))
        conn.commit()

        if c.rowcount > 0:
            conn.close()
            return jsonify("Successfully updated the quantity and name")

        conn.close()
        return jsonify("Id not found")

@app.route("/order", methods=["POST"])
def orderDish():
    if request.method == "POST":
        data = request.get_json()
        conn, c = get_db()
        c.execute("SELECT * FROM dish WHERE Name=?", (data['food'],))
        dish = c.fetchone()
        if dish:
            if dish['Quantity'] >= data['Quantity']:
                price = dish['Price'] * data['Quantity']
                c.execute("INSERT INTO orders (Name, Quantity, Price, Status) VALUES (?, ?, ?, ?)",
                          (dish['Name'], data['Quantity'], price, "received"))
                conn.commit()
                conn.close()
                return jsonify("Order Created Successfully")
            else:
                conn.close()
                return jsonify("Insufficient quantity of the dish")

        conn.close()
        return jsonify("Food not found")



@app.route("/allorder", methods=["GET"])
def getOrder():
    conn, c = get_db()
    c.execute("SELECT * FROM orders")
    data = c.fetchall()
    result = []
    for item in data:
        result.append({
            'id': item[0],
            'Name': item[1],
            'Quantity': item[2],
            'Price': item[3],
            'Status': item[4]
        })
    conn.close()
    return jsonify(result)

@app.route("/login", methods=["POST"])
def getlogin():
    logindata = request.get_json()
    conn, c = get_db()
    c.execute("SELECT * FROM login WHERE email=? AND password=?", (logindata['email'], logindata['password']))
    login = c.fetchone()

    if login:
        conn.close()
        return jsonify("Login Successful", logindata)

    conn.close()
    return jsonify("Wrong Credentials", "")

@app.route("/Signup", methods=["POST"])
def getSignup():
    signup = request.get_json()
    print(signup)  # Add this line to print the signup data
    conn, c = get_db()
    c.execute("SELECT * FROM login WHERE email=?", (signup['email'],))
    existing_user = c.fetchone()

    if existing_user:
        conn.close()
        return jsonify("Email already exists")

    c.execute("INSERT INTO login (name, email, password) VALUES (?, ?, ?)", (signup['name'], signup['email'], signup['password']))
    conn.commit()
    conn.close()
    return jsonify("Successfully Created Account")






@app.route("/updateOrder/<string:name>", methods=["PATCH"])
def updateOrder(name):
    conn, c = get_db()
    c.execute("SELECT * FROM orders WHERE Name=?", (name,))
    order = c.fetchone()

    if order:
        if order[4] == "received":
            c.execute("UPDATE orders SET Status=? WHERE Name=?", ("preparing", name))
            conn.commit()
            conn.close()
            return jsonify("Order Status changed successfully: Preparing")
        elif order[4] == "preparing":
            c.execute("UPDATE orders SET Status=? WHERE Name=?", ("ready for pickup", name))
            conn.commit()
            conn.close()
            return jsonify("Order Status changed successfully: Ready for Pickup")
        elif order[4] == "ready for pickup":
            c.execute("UPDATE orders SET Status=? WHERE Name=?", ("delivered", name))
            conn.commit()
            conn.close()
            return jsonify("Order Status changed successfully: Delivered")
        else:
            conn.close()
            return jsonify("Order already delivered")

    conn.close()
    return jsonify("Order with this name doesn't exist")

# Rest of your code...

if __name__ == '__main__':
    app.run(port=8080)
