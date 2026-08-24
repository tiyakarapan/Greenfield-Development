from flask import Flask, request
from flask_cors import CORS
from .json_provider import apply_custom_json_provider

class App:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        apply_custom_json_provider(self.app)

    def run(self, port: int):
        self.app.run(debug=True, port=port)

    def get(self, url: str):
        route = self._prefix_url(url)
        return self.app.route(route, methods=["GET"])

    def post(self, url: str):
        route = self._prefix_url(url)
        return self.app.route(route, methods=["POST"])

    def put(self, url: str):
        route = self._prefix_url(url)
        return self.app.route(route, methods=["PUT"])

    def delete(self, url: str):
        route = self._prefix_url(url)
        return self.app.route(route, methods=["DELETE"])

    def get_request_body(self):
        return request.get_json()

    def _prefix_url(self, url: str):
        if not url.startswith("/"):
            url = "/" + url

        return f"/api{url}"
        