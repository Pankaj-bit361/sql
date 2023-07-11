from flask import Flask, jsonify, request

app = Flask(__name__)

post_arr=[]


@app.route('/', methods=["GET"])
def get():
    return jsonify('Hello world')

@app.route('/get', methods=["GET"])
def gets():
    return jsonify(post_arr)


@app.route('/posts', methods=["POST"])
def post():
    if request.method == "POST":
      data = request.get_json()
      obj={
          "username": data["username"],
          "caption": data["caption"],
          "likes": data["likes"],
          "id": data["id"],
          "comments":[]
      }
      post_arr.append(obj)
      return jsonify("data added successfully")
    

@app.route('/delete/<int:Id>', methods=["DELETE"])
def delete(Id):
    if request.method == "DELETE":

        for i in post_arr:
            if i["id"] == Id:
                post_arr.remove(i)
                return jsonify("Item deleted successfully")
            
    return jsonify("Post does't exists")


@app.route('/increase_like/<int:Id>', methods=["PATCH"])
def increase_like(Id):
    if request.method == "PATCH":

        for i in post_arr:
            print(i)
            if i["id"] == Id:
                i["likes"] = i["likes"] + 1
                return jsonify("Likes increased successfully")
            
    return jsonify("Post is not found!!")


@app.route('/increase_comment/<int:Id>', methods=["PATCH"])
def increase_comment(Id):
    if request.method == "PATCH":
        data = request.get_json()

        for i in post_arr:
            if i["id"] == Id:
                i["comments"].append(data["comment"])
                return jsonify("Comment added")
            
    return jsonify("Post is not found!!")











if __name__ == "__main__":
    app.run(debug=True)