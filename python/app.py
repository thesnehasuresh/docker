from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Dockerized Python Application based on Flask. I am creating repos on Git for demonstrating docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
