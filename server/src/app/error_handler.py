from flask import Flask
from werkzeug.exceptions import HTTPException

def apply_error_handler(app: Flask):
    def unhandled_exception_handler(e):
        if isinstance(e, HTTPException):
            return {
                "error": e.name,
                "message": e.description,
                "code": e.code
            }, e.code
            
        print(str(e))
        return { "message": "Something went wrong" }, 500

    app.register_error_handler(Exception, unhandled_exception_handler)