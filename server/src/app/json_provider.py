from flask import Flask
from flask.json.provider import DefaultJSONProvider
from datetime import date


class CustomJSONProvider(DefaultJSONProvider):
    @staticmethod
    def default(obj):
        if isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")

        return super(CustomJSONProvider, CustomJSONProvider).default(obj)


def apply_custom_json_provider(app: Flask):
    app.json_provider_class = CustomJSONProvider
    app.json = CustomJSONProvider(app)