from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/',method=["GET"])
def get():
    return jsonify("This is blog page")


if __name__ == "__main__":
    app.run(debug=True)







