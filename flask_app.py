from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    # Run Flask development server
    app.run(host="127.0.0.1", port=5000, debug=True)