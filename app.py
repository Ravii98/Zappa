from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Hello from Flask & Zappa POC!")

# This is the handler Zappa will look for
def lambda_handler(event, context):
    from zappa.handler import lambda_handler as zappa_handler
    return zappa_handler(event, context)
