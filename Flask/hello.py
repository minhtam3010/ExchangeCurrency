from unicodedata import name
from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>&<age>")
def user(name: str, age: int):
    return f"""
            <h1>Hello {name}!</h1>
            <h2>Your age is {age}</h2>
            """

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)