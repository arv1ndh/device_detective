from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"

@app.route("/ua")
def useragent_extractor():
    ua = request.headers.get("user-agent")
    display_message = f"The User Agent is {ua}"
    return display_message
