from flask import Flask
app = Flask(__name__)

data = []

@app.route('/')
def hello():
    while True:
        data.append("A" * 10**7)
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
