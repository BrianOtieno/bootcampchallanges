from flask import Flask,request, session, jsonify, json
import re
import datetime

app=Flask(__name__,static_url_path="")
app.secret_key = "bootcamp-key"

#Define Default Version
default_api_version = 1

diary_info = {}
userdata = {}
home_data = {}


@app.route("/api", methods=["GET"])
def index():

    # Assign the API version. Default to V1 or a specified higher

    available_versions = [{"2018.24": "Version 1"}]

    return jsonify({"message":"{} -OK : API Home: Available API Versions {}".
    format(200, available_versions
    )})


@app.route("/api/register", methods=['POST'])
def register():
    # Assign the API version. Default to V1 or a specified higher
    if request.get_json()["version"]:
        version = request.get_json()["version"]
    else:
        version = default_api_version

    if version == 1:

        user_info = request.get_json()
        firstname = user_info["firstname"]
        lastname = user_info["lastname"]
        email = user_info["email"]
        username = user_info["username"]
        password = user_info["password"]
        confirm_password = user_info["confirm_password"]


        if not firstname or not lastname or not email or not username or not \
        password or not confirm_password:
            return jsonify({"message": "Error {} - Length Required : All \
            fields are mandatory". format(411)})

        elif password != confirm_password:
            return jsonify({"message": "Error {} - Precondition Failed  :\
            Password and Confirm password not matching". format(412)})

        elif username in userdata:
            return jsonify({"message": "Error {} - Conflict  : User already \
            registered". format(409)})

        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",
        email):
            return jsonify({"message": "{} - Expectation Failed: Email must \
            be valid".format(417)})

        else:
            userdata[username] = {"first name": firstname,
            "last name": lastname, "email": email, "username": username,
            "password": password,"confirm_password": confirm_password}

            return jsonify({"message": "{} - OK : Registered Users: {}". \
            format(200, userdata)})

    return jsonify({"message": "API Version specified unsuported!"})

@app.route("/api/v1/login", methods=["POST"])
def login():
    # Assign the API version. Default to V1 or a specified higher
    # Route can be set to /api/login
    if request.get_json()["version"]:
        version = request.get_json()["version"]
    else:
        version = default_api_version

    if version == 1:

        user_info = request.get_json()
        username = user_info["username"]
        password = user_info["password"]

        if not password or not username:
            return jsonify({"message": "Error {} - Length Required : Both \
            fields are required". format(411)})

        elif username not in userdata:
            #keep them guesing which is invalid - for security
            return jsonify({"message": "{} - Unauthorized: Either username \
            or password not valid".format(401)})

        elif username in userdata and \
        password == userdata[username]["password"]:
            session["username"] = username
            session["logged_in"] = True
            return jsonify({"message": "{} - OK: Logged in successfully". \
            format(200)})

        else:
            return jsonify({"message": "{} - Unauthorized: invalid \
            credenatials".format(401)})

    return jsonify({"message": "API Version specified unsuported!"})
#return jsonify({"message": type(user_info)})

@app.route("/api/v1/entries", methods=['GET','POST'])
def entry():

    if request.method =="POST":
        # Assign the API version. Default to V1 or a specified higher
        # Route can be set to /api/entry
        if request.get_json()["version"]:
            version = request.get_json()["version"]
        else:
            version = default_api_version

        username = session.get('username')
        entry = request.get_json()["entry"]
        entry_date = datetime.datetime.now()
        event_date = request.get_json()["event_date"]
        notification_date = request.get_json()["notification_date"]

        #Generate unique entry id (username concatenated with curr date)
        entry_id = username + str(entry_date)

        if username not in userdata:
            return jsonify({"message": "{} - Unauthorized: Login \
            required".format(401)})

        elif not entry or not event_date or not notification_date:
            return jsonify({"message": "Error {} - Length Required : All \
            fields are mandatory". format(411)})

        elif entry_id in diary_info:
            return jsonify({"message": "Error {} - Conflict  : This entry \
            already exist". format(409)})

        else:
            diary_info[entry_id] = {"entry": entry,"entry date": entry_date,
            "Event Date": event_date, "username": username,
            "Notification Date": notification_date}

            return jsonify({"message": "{} - OK : Entry Posted: {}". \
            format(200, diary_info)})

    if request.method =="GET":
        return jsonify({"message": "{} - OK : Entries : {}". \
        format(200, diary_info)})

    else:
        return jsonify({"message": "Version specified unsuported!"})


if __name__=='__main__':
    app.run(debug=True)
