""" module that contain endpoints """
from flask import Flask, request, session, jsonify, json
from .main.user import User
import re

app = Flask(__name__)
app.secret_key = "string"
users = []


@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    """ Takes request and return a necessary response"""
    json_dict = request.get_json()
    name = json_dict["name"]
    email = json_dict["email"]
    print("======> reg email", json_dict['email'])
    password = json_dict['password']
    confirm = json_dict["confirm"]
    category = json_dict["category"]
    if name and not isinstance(name, str):
        error = {"message": "Invalid name"}
        return jsonify(error)
    if email and not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        error = {"message": "Invalid Email"}
        return jsonify(error)
    if password and len(password) < 7:
        error = {"message": "Password too short"}
        return jsonify(error)
    if password != confirm:
        error = {"message" : "password dont match"}
        return jsonify(error)
    if category and not isinstance(category, str):
        error = {"message": "invalid category"}
        return jsonify(error)
    new_user = User(name, email, password, category)
    users.append(new_user)
    message = {"message": "successfully registered"}
    response = jsonify(message)
    response.status_code = 201
    return response


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """Takes a request and returns a json response"""
    json_dict = request.get_json()
    email = json_dict["email"]
    print("===>", json_dict["email"])
    password = json_dict["password"]
    for user in users:
        if email and user.email != email:
            message = {"error": "email dont match"}
            return jsonify(message)
        if password and user.password != password:
            message = {"error": "Password do not match"}
            return jsonify(message)
        else:
            message = {"message": "Successfully logged in"}
            session["user_id"] = user._id
            response = jsonify(message)
            response.status_code = 200
            return response
    return jsonify(message)


@app.route("/api/v1/events", methods=['POST'])
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
    if not users:
        message = "Login first"

    for user in users:
        if user._id == session["user_id"]:
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
                              location, user._id)
            message = {"message": " event succesfully created "}
            response = jsonify(message)
            response.status_code = 201
            return response
    return jsonify(message)


@app.route("/api/v1/events", methods=["GET"])
def view_events():
    """ gets the events that were created """
    if not users:
        response = "Login first"
    for user in users:
        if user._id == session["user_id"]:
            events = [event.events_data() for event in user.events.values()]
            response = {"events": events}
    return jsonify(response)


@app.route("/api/v1/events/<eventId>", methods=["PUT"])
def update_event(eventId):
    """ edits events matching the eventId passed """
    json_dict = request.get_json()
    name = json_dict["name"]
    description = json_dict["description"]
    category = json_dict["category"]
    date = json_dict["date"]
    author = json_dict["author"]
    location = json_dict["location"]
    if not users:
        message = "Login first"
    for user in users:
        if user._id == session["user_id"]:
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
            user.update_event(eventId, name, description, category, date,
                              author, location)
            message = {"message": " event successfully edited"}
            response = jsonify(message)
            response.status_code = 200
            return response
    return jsonify(message)


@app.route("/api/v1/events/<eventId>", methods=["DELETE"])
def delete_event(eventId):
    """ deletes events matching the eventId """
    if not users:
        message = "Login first"
    for user in users:
        if user._id == session["user_id"]:
            user.delete_event(eventId)
            message = {" message ": "event deleted"}
            response = jsonify(message)
            response.status_code = 200
            return response

        return jsonify(message)


@app.route("/api/v1/event/<eventId>/rsvp", methods=["POST"])
def create_rsvp(eventId):
    """ creates rsvp for particular event matching the eventId passed"""
    json_dict = request.get_json()
    name = json_dict["name"]
    email = json_dict["email"]
    phone_no = json_dict["phone_no"]
    category = json_dict["category"]
    if not users:
        message = "Login first"
    for user in users:
        if user._id == session["user_id"]:
            if name and not isinstance(name, str):
                error = {"message": "Invalid name"}
                return jsonify(error)
            if email and \
                not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
                error = {"message": "Invalid Email"}
                return jsonify(error)
            if phone_no and len(phone_no) < 10:
                error = {"message": "phone_no too short"}
                return jsonify(error)
            for value in user.events.values():
                if eventId == value._id:
                    value.add_rsvp(name, email, phone_no, category)
                    message = {"message": "rsvp created successfully"}
                    response = jsonify(message)
                    response.status_code = 201
                    return response
    return jsonify(message)


@app.route("/api/v1/event/<eventId>/rsvp", methods=["GET"])
def rsvps(eventId):
    """ gets the rsvps for each event according to the eventId """
    if not users:
        message = "login first"
    for user in users:
        if user._id == session["user_id"]:
            for key, val in user.events.items():
                if eventId == key:
                    rsvps = [rsvp.rsvps_data() for rsvp in val.rsvps.values()]
                    message = {"rsvps": rsvps}
                    response = jsonify(message)
                    response.status_code = 200
                    return response
            return jsonify(response)


@app.route("/api/v1/event/<eventId>/rsvp/<rsvpId>", methods=["PUT"])
def update_rsvp(eventId, rsvpId):
    """ edits the rsvps for each event according to the rsvpId """
    json_dict = request.get_json()
    name = json_dict["name"]
    email = json_dict["email"]
    phone_no = json_dict["phone_no"]
    category = json_dict["category"]
    message = None
    if not users:
        message = "login first"
    for user in users:
        if user._id == session["user_id"]:
            if name and not isinstance(name, str):
                error = {"message": "Invalid name"}
                return jsonify(error)
            if email and \
                not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
                error = {"message": "Invalid Email"}
                return jsonify(error)
            if phone_no and len(phone_no) < 10:
                error = {"message": "phone_no too short"}
                return jsonify(error)
            for key, val in user.events.items():
                if eventId == key:
                    for keys, vals in val.rsvps.items():
                        if keys == rsvpId:
                            val.update_rsvp(rsvpId, name, email, phone_no,
                                            category)
                            message = {"message": " rsvp successfully edited"}
                            response = jsonify(message)
                            response.status_code = 200
                            return response

        return jsonify(message)
    return jsonify(message)


@app.route("/api/v1/event/<eventId>/rsvp/<rsvpId>", methods=["DELETE"])
def delete_rsvp(eventId, rsvpId):
    """ deletes rsvps according to the rsvpId"""
    if users:
        message = "login first"
    for user in users:
        if user._id == session["user_id"]:
            for key, val in user.events.items():
                if eventId == key:
                    for keys, vals in val.rsvps.items():
                        if keys == rsvpId:
                            val.delete_rsvp(rsvpId)
                            return jsonify({"message": "rsvp successfully deleted"})
                            response = jsonify(message)
                            response.status_code = 200
                            return response

    return jsonify(message)


@app.route("/api/v1/logout", methods=["POST"])
def logout():
    """ removes the user_id session """
    session.clear()
    response = "successfully logout"
    return jsonify(response)
