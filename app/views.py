"""Module that contain endpoints."""
import re
from flask import Flask, request, session, jsonify
from .main.user import User

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = "string"
users = []


@app.errorhandler(404)
def not_found(error):
    """Handle 404 error."""
    response = jsonify({"message": "Sorry the url does not exists"})
    response.status_code = 404
    return response


@app.errorhandler(500)
def handle_server_error(error):
    """Handle 500 error."""
    response = jsonify(
        {"message": "oops! something went wrong with the application"})
    response.status_code = 500
    return response


@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    """Take request and return a necessary response."""
    json_dict = request.get_json()
    name = json_dict["name"]
    email = json_dict["email"]
    password = json_dict['password']
    confirm = json_dict["confirm"]
    category = json_dict["category"]
    if name.strip() == "" or not name.isalpha():
        error = {"message": "Invalid name"}
        return jsonify(error)
    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        error = {"message": "Invalid Email"}
        return jsonify(error)
    if len(password) < 7:
        error = {"message": "Password too short"}
        return jsonify(error)
    if password != confirm:
        error = {"message": "password dont match"}
        return jsonify(error)
    if category.strip() == "" and not category.isalpha():
        error = {"message": "invalid category"}
        return jsonify(error)
    for user in users:
        if user.email == email:
            return jsonify({"message": "email already exists try again"})
    user = User(name, email, password, category)
    users.append(user)
    message = {"message": "successfully registered"}
    response = jsonify(message)
    response.status_code = 201
    return response


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    """Take a request and returns a json response."""
    if session:
        logout()
    json_dict = request.get_json()
    email = json_dict["email"]
    password = json_dict["password"]
    for user_data in users:
        if email == user_data.email:
            if user_data.password == password:
                session["user_id"] = user_data._id
                message = {"message": "Successfully logged in"}
                response = jsonify(message)
                response.status_code = 200
                return response
        message = {"message": "invalid credentials"}
        response = jsonify(message)
        response.status_code = 403
        return response
    return jsonify(response)


@app.route("/api/v1/events", methods=['POST'])
def create_event():
    """Take a request and return a json response."""
    json_dict = request.get_json()
    name = json_dict["name"]
    description = json_dict["description"]
    category = json_dict["category"]
    date = json_dict["date"]
    author = json_dict["author"]
    location = json_dict["location"]
    message = None
    if not users:
        response = {"message": "Login first"}
    for user in users:
        if user._id == session["user_id"]:
            if name.strip() == "" or not name.isalpha():
                message = {"message": "invalid name"}
                return jsonify(message)
            if description.strip() == "" or not description.isalpha():
                message = {"message": "invalid description"}
                return jsonify(message)
            if category.strip() == "" or not category.isalpha():
                message = {"message": "invalid category"}
                return jsonify(message)
            if not isinstance(date, str):
                message = {"message": "invalid date"}
            if not isinstance(date, str):
                return jsonify(message)
            if author.strip() == "" or not author.isalpha():
                message = {"message": "invalid author"}
                return jsonify(message)
            if location.strip() == "" or not location.isalpha():
                message = {"message": "invalid location"}
                return jsonify(message)
            user.create_event(name, description, category, date, author,
                              location, user._id)
            response = jsonify({"message": " event succesfully created "})
            response.status_code = 201
            return response
    return jsonify(response)


@app.route("/api/v1/events", methods=["GET"])
def view_events():
    """Get the events that were created."""
    if not users:
        response = {"message": "Login first"}
    for user in users:
        if user._id == session["user_id"]:
            events = [event.events_data() for event in user.events.values()]
            message = {"events": events}
            response = jsonify(message)
            response.status_code = 200
            return response
    return jsonify(response)


@app.route("/api/v1/events/<eventId>", methods=["PUT"])
def update_event(eventId):
    """Edit events matching the eventId passed."""
    json_dict = request.get_json()
    name = json_dict["name"]
    description = json_dict["description"]
    category = json_dict["category"]
    date = json_dict["date"]
    author = json_dict["author"]
    location = json_dict["location"]
    if not users:
        response = {"message": "Login first"}
    for user in users:
        if user._id == session["user_id"]:
            if name.strip() == "" or not name.isalpha():
                message = {"message": "invalid name"}
                return jsonify(message)
            if description.strip() == "" or not description.isalpha():
                message = {"message": "invalid description"}
                return jsonify(message)
            if category.strip() == "" or not category.isalpha():
                message = {"message": "invalid category"}
                return jsonify(message)
            if not isinstance(date, str):
                message = {"message": "invalid date"}
                return jsonify(message)
            if author.strip() == "" or not author.isalpha():
                message = {"message": "invalid author"}
                return jsonify(message)
            if location.strip() == "" or not location.isalpha():
                message = {"message": "invalid location"}
                return jsonify(message)
            user.update_event(eventId, name, description, category, date,
                              author, location)
            message = {"message": " event successfully edited"}
            response = jsonify(message)
            response.status_code = 200
            return response
    return jsonify(response)


@app.route("/api/v1/events/<eventId>", methods=["DELETE"])
def delete_event(eventId):
    """Delete events matching the eventId."""
    if not users:
        response = {"message": "Login first"}
    for user in users:
        if user._id == session["user_id"]:
            user.delete_event(eventId)
            message = {" message ": "event deleted"}
            response = jsonify(message)
            response.status_code = 202
            return response

        return jsonify(response)


@app.route("/api/v1/event/<eventId>/rsvp", methods=["POST"])
def create_rsvp(eventId):
    """Create rsvp for particular event matching the eventId passed."""
    json_dict = request.get_json()
    name = json_dict["name"]
    email = json_dict["email"]
    phone_no = json_dict["phone_no"]
    category = json_dict["category"]
    if not users:
        response = {"message": "Login first"}
    for user in users:
        if user._id == session["user_id"]:
            if name.strip() == "" or not name.isalpha():
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
    return jsonify(response)


@app.route("/api/v1/event/<eventId>/rsvp", methods=["GET"])
def rsvps(eventId):
    """Get the rsvps for each event according to the eventId."""
    if not users:
        response = {"message": "Login first"}
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
    """Edit the rsvps for each event according to the rsvpId."""
    json_dict = request.get_json()
    name = json_dict["name"]
    email = json_dict["email"]
    phone_no = json_dict["phone_no"]
    category = json_dict["category"]
    message = None
    if not users:
        response = {"message": "Login first"}
    for user in users:
        if user._id == session["user_id"]:
            if name.strip() == "" or not name.isalpha():
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

    return jsonify(response)


@app.route("/api/v1/event/<eventId>/rsvp/<rsvpId>", methods=["DELETE"])
def delete_rsvp(eventId, rsvpId):
    """Deletes rsvps according to the rsvpId."""
    if not users:
        response = {"message": "Login first"}
    for user in users:
        if user._id == session["user_id"]:
            for key, val in user.events.items():
                if eventId == key:
                    for keys, vals in val.rsvps.items():
                        if keys == rsvpId:
                            val.delete_rsvp(rsvpId)
                            return jsonify({
                                "message":
                                "rsvp successfully deleted"
                            })
                            response = jsonify(message)
                            response.status_code = 202
                            return response

    return jsonify(response)


@app.route("/api/auth/reset-password/", methods=["PUT"])
def reset_password():
    """Resets an existing users password."""
    json_dict = request.get_json()
    email = json_dict["email"]
    new_password = json_dict["new_password"]
    for user in users:
        if user.email == email:
            user.password = new_password
            message = {"message": "password successfully reset"}
            response = jsonify(message)
            response.status_code = 200
            return response
    return jsonify(response)


@app.route("/api/v1/logout", methods=["POST"])
def logout():
    """Removes the user_id session."""
    if not users:
        response = {"message": "Login first"}
    for user in users:
        session.clear()
        message = {"message": "successfully logout"}
        response = jsonify(message)
        response.status_code = 200
        return response
    return jsonify(response)
