""" module that contain endpoints """
from flask import Flask, request, session, jsonify
from .main.user import User
import re

app = Flask(__name__)
app.secret_key = "string"
users= []


@app.route('/api/v1/auth/register', methods=['POST', 'GET'])
def register():
    """ Takes request and return a necessary response"""
    json_dict = request.get_json()
    name = json_dict["name"]
    email = json_dict["email"]
    password = json_dict['password']
    category = None
    if name and not isinstance(name, str):
        error = {"message": "Invalid name"}
        return jsonify(error)
    if email and \
        not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        error = {"message": "Invalid Email"}
        return jsonify(error)
    if password and len(password) < 7:
        error = {"message": "Password too short"}
        return jsonify(error)
    if category and not isinstance(category, str):
        error = {"message": "invalid category"}
        return jsonify(error)
    new_user = User(password, name, email, category)
    users.append(new_user)
    session['email'] = new_user.email
    data = {"name": new_user.name,
            "email": email,
            "password": password,
            "category": new_user.rsvp_category}
    return jsonify(data)


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """Takes a request and returns a json response"""
    json_dict = request.get_json()
    email = json_dict["email"]
    password = json_dict["password"]
    message = None
    logged_email = None
    print(".....>>>", logged_email)
    for user in users:
        if email and user.email != email:
            message = {
                "error": "email dont match"
            }
            return jsonify(message)
        if password and user.password != password:
            message = {
                "error": "Password do not match"
            }
            return jsonify(message)
        else:
            message = {
                "message": "Successfully logged in"
            }
            logged_email = user.email
            print("..======...>>>", logged_email)
            return jsonify(message)

    session["logged_email"] = logged_email
    return jsonify(message)
