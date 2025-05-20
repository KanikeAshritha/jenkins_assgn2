from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet(name="World"):
    """Return a greeting message."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    print(greet())
    app.run(host="0.0.0.0", port=5000)
    