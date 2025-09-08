from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/hello")
def hello():
    """
    Example endpoint returning a message
    ---
    responses:
      200:
        description: A simple hello
    """
    return jsonify(message="Hello from Flask with Swagger!")

if __name__ == "__main__":
    app.run()
