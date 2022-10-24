from flask import Flask, make_response, redirect, abort

app = Flask(__name__)

@app.route("/user/<name>&<age>")
def user(name: str, age: int):
    return f"""
            <h1>Hello {name}!</h1>
            <h2>Your age is {age}</h2>
            """

@app.route("/some/<user_id>")
def something(user_id: int):
    if user_id != "1":
        abort(404)
    return "<h1>AAAA</h1>"

if __name__ == "__main__":
    app.run(debug=True)