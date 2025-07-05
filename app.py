from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"
@app.route('/info')
def info():
    return "This is an informational page."
@app.route('/reverse/<text>')
def reverse(text):
    return text[::-1]

@app.route("/calc/<int:a>/<int:b>")
def calc(a, b):
    result = a + b
    return f"The sum of {a} and {b} is {result}."

@app.route('/user/<string:name>/<int:age>')
def user(name, age):
    return f"Hello, {name}. You are {age} years old."

if __name__ == "__main__":
    app.run(debug=True)
