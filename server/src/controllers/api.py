from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def _prefix_url(url: str):
    if not url.startswith("/"):
        url = "/" + url

    return f"/api{url}"

def api_get(url: str):
    return app.route(_prefix_url(url), methods=["GET"])

def api_post(url: str):
    return app.route(_prefix_url(url), methods=["POST"])

def api_put(url: str):
    return app.route(_prefix_url(url), methods=["PUT"])

def api_delete(url: str):
    return app.route(_prefix_url(url), methods=["DELETE"])

def get_request_body():
    return request.get_json()