from flask import Flask

if __name__ == "__main__":
    Flask.app.run(host="127.0.0.1", port=8080, debug=True)

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"
