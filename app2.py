from flask import Flask

app = Flask(__name__)

@app.route("/calc/<int:a>/<int:b>")
def calc(a, b):
    result = a + b
    return f"The sum of {a} and {b} is {result}."

if __name__ == "__main__":
    app.run(debug=True)
