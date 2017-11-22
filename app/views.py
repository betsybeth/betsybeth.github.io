""" module that contain endpoints """
from flask import Flask, request
from main.user import User

app = Flask(__name__)
app.secret_key = "string"


if __name__== '__main__':
    app.run(debug=True)
