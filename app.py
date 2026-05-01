from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Restart Success 🚀"

if __name__ == "__main__":
    app.run(debug=True, port=5000)