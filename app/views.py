""" module that contain endpoints """
from flask import Flask, request, session, jsonify, json
from .main.user import User
import re

app = Flask(__name__)
app.secret_key = "string"
users = []


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
    data = {
        "name": new_user.name,
        "email": new_user.email,
        "password": new_user.password,
        "category": new_user.rsvp_category
    }
    return jsonify(data)


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """Takes a request and returns a json response"""
    json_dict = request.get_json()
    email = json_dict["email"]
    password = json_dict["password"]
    message = None
    logged_email = None
    for user in users:
        if email and user.email != email:
            message = {"error": "email dont match"}
            return jsonify(message)
        if password and user.password != password:
            message = {"error": "Password do not match"}
            return jsonify(message)
        else:
            message = {"message": "Successfully logged in"}
            logged_email = user.email
            return jsonify(message)
    session["email"] = logged_email
    return jsonify(message)


@app.route("/api/v1/create_event", methods=['POST'])
def create_event():
    """ Takes a request and return a json response """
    json_dict = request.get_json()
    name = json_dict["name"]
    description = json_dict["description"]
    category = json_dict["category"]
    date = json_dict["date"]
    author = json_dict["author"]
    location = json_dict["location"]
    message = None

    for user in users:
        if user.email == session["email"]:
            if name and not isinstance(name, str):
                message = {"message": "invalid name"}
                return jsonify(message)
            if description and not isinstance(description, str):
                message = {"message": "invalid description"}
                return jsonify(message)
            if category and not isinstance(category, str):
                message = {"message": "invalid category"}
                return jsonify(message)
            if date and not isinstance(date, str):
                message = {"message": "invalid date"}
                return jsonify(message)
            if author and not isinstance(author, str):
                message = {"message": "invalid author"}
                return jsonify(message)
            if location and not isinstance(location, str):
                message = {"message": "invalid location"}
                return jsonify(message)
            user.create_event(name, description, category, date, author,
                              location)
            message = {"message": " event succesfully created "}
    return jsonify(message)


@app.route("/api/v1/events", methods=["GET"])
def events():
    for user in users:
        if user.email == session["email"]:
            events = user.events
    return jsonify({"events": events})


@app.route("/api/v1/update_event/<_id>", methods=["PUT"])
def update_event(_id):
    json_dict = request.get_json()
    name = json_dict["name"]
    description = json_dict["description"]
    category = json_dict["category"]
    date = json_dict["date"]
    author = json_dict["author"]
    location = json_dict["location"]
    message = None
    for user in users:
        if user.email == session["email"]:
            user.update_event(_id, name, description, category, date, author,
                              location)
            message = {"message": " event successfully edited"}
        return jsonify(message)
