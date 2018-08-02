from flask import Flask,request, session, jsonify, json
import re, random, psycopg2, datetime, uuid
from werkzeug import generate_password_hash, check_password_hash
from functools import wraps
import jwt, os
from dbschema import Registration
from instance.config import app_config

app=Flask(__name__,static_url_path="", instance_relative_config=True)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config.from_pyfile('config.py')

#Connection To DB for CRUD For Heroku
dbname = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

#Connection To DB for CRUD For Heroku
dbname = "andelabootcamp"
host = "localhost"
user = "postgres"
password = "5ure5t@re!"
port = "5432"
conn = psycopg2.connect("dbname = {} user={} host={} \
password={} port={}".format(dbname, user, host, password, port))
conn.autocommit = True
cur = conn.cursor()

cur = conn.cursor()
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])

            cur.execute("SELECT * FROM users WHERE public_id = %s",[data['public_id']])
            user = cur.fetchone()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(user, *args, **kwargs)

    return decorated


class DbConnection:
    def __init__(self):
        try:
            print("############ GENERATING SCHEMA ##################")
            self.connection = psycopg2.connect("dbname = 'andelabootcamp'\
            user='postgres' host='localhost' password='5ure5t@re!'\
             port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except Exception as e:
            print("############ FAILED TO GENERATE SCHEMA ##################")
            return jsonify({"Error Message": e.message} )


    def create_users_table(self):
        print ("==> Creating Users Table")
        users_table_command = "CREATE TABLE IF NOT EXISTS users(\
          uid serial PRIMARY KEY,\
          firstname VARCHAR(50) not null,\
          lastname VARCHAR(50) not null,\
          email VARCHAR(100) not null unique,\
          username VARCHAR(100) not null unique,\
          password VARCHAR(128) not null,\
          public_id VARCHAR(128)\
        )"
        self.cursor.execute(users_table_command)
        print ("==> Created Users Table successfully")

    def create_diary_table(self):
        print ("==> Creating Diaries Table")
        diary_table_command = "CREATE TABLE IF NOT EXISTS diary(\
          did serial PRIMARY KEY,\
          username VARCHAR(100) not null,\
          entry TEXT,\
          event_date DATE, \
          entry_date DATE,\
          notification_date DATE,\
          FOREIGN KEY (username) REFERENCES users(username)\
          ON UPDATE CASCADE ON DELETE RESTRICT\
        )"
        self.cursor.execute(diary_table_command)
        print ("==> Diaries Table Created successfully")


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

        # elif username in userdata:
        #     return jsonify({"message": "Error {} - Conflict  : User already \
        #     registered". format(409)})

        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",
        email):
            return jsonify({"message": "{} - Expectation Failed: Email must \
            be valid".format(417)})


        public_id = str(uuid.uuid4())
        # register_user = Registration(firstname, lastname, email, username,
        #  password, public_id)
        #
        # if register_user.register(firstname, lastname, email, username,
        #  password, public_id):
        #     return jsonify({'message' : 'User Registered!'})
        # return jsonify({'message' : 'Database error occured!'})
        try:
            cur.execute("INSERT INTO users(firstname, lastname, email,\
            username, password, public_id)\
             VALUES('{}','{}','{}','{}','{}', '{}')".format(
            firstname, lastname, email, username, password, public_id
            ))
            return jsonify({"message": "User Registered Users"}),200

        except Exception as e:
            return jsonify({"message": "Database error: {}".format(
            e.message
            )}),200

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
            return jsonify({"message": "Error : Length Required : Both \
            fields are required"}), 411

        cur.execute("SELECT * FROM users \
        WHERE username='{}' AND password='{}'".format(username, password))

        user = cur.fetchone()

        if user:
            session['username'] = username
            auth = request.authorization
            public_id = user[6]
            token = jwt.encode({'public_id' : public_id,
            'exp' : datetime.datetime.utcnow() +
            datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({"message":"Login successfull",
            'token': token.decode('UTF-8')}),200
        #keep them guesing which is invalid - for security
        return jsonify({"message": "Unauthorized: Either username \
        or password not valid"}),401



    # logic for the next API Version

    return jsonify({"message": "API Version specified unsuported!"})

@app.route("/api/v1/entries", methods=['GET','POST'])
@token_required
def entry(user):

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
        #entry_id = str(username) + str(entry_date)

        if username not in session['username']:
            return jsonify({"message": "{} - Unauthorized: Login \
            required".format(401)})

        elif not entry or not event_date or not notification_date:
            return jsonify({"message": "Error {} - Length Required : All \
            fields are mandatory". format(411)})

        else:
            cur.execute("INSERT INTO diary(username, entry, event_date,\
            entry_date, notification_date) VALUES('{}','{}','{}',\
            '{}','{}')".format(username, entry, event_date, entry_date,
             notification_date))
            return jsonify({"message": "Entry inserted!"}),200

    if request.method =="GET":
        cur.execute("SELECT * FROM diary")
        query_result = cur.fetchall()
        if not query_result:
            return jsonify({"message": "Entries not found"}),404
        return jsonify(query_result),200
    else:
        return jsonify({"message": "Version specified unsuported!"})

@app.route("/api/v1/entry/<int:entry_id>", methods=['PUT','GET', 'DELETE'])
@token_required
def entry_actions(user, entry_id):
    entry_id = entry_id
    if request.method =="PUT":
        # Assign the API version. Default to V1 or a specified higher
        # Route can be set to /api/entry/<int : entry_id>
        if request.get_json()["version"]:
            version = request.get_json()["version"]
        else:
            version = default_api_version

        if version == 1:
            username = session.get('username')
            entry = request.get_json()["entry"]
            entry_date = datetime.datetime.now()
            event_date = request.get_json()["event_date"]
            notification_date = request.get_json()["notification_date"]


            try:
                cur.execute("UPDATE diary  SET username = '{}', \
                entry = '{}', entry_date = '{}', event_date = '{}',\
                notification_date = '{}' WHERE did = {}".format(
                username, entry, entry_date, event_date, notification_date,
                entry_id ))
                return jsonify({"message": "Entry Updated!"}),200
            except Exception as e:
                return jsonify({"Error Message": e.message} )

            return jsonify({"message": "{} - Not Found: The entry  \
            requested not found".format(404)})

        # PUT logic for the next API Version

        return jsonify({"message": "Version specified unsuported!"})

    if request.method =="GET":
        cur.execute("SELECT * FROM diary WHERE did = {}".format(entry_id))
        query_result = cur.fetchall()
        if not query_result:
            return jsonify({"message": "Entries not found"}),404
        return jsonify(query_result),200

    if request.method == "DELETE":
        try:
            cur.execute("DELETE FROM diary WHERE did = {}".format(entry_id))
            return jsonify({"message": "Entry Deleted"}),200
        except:
            return jsonify({"message": "Entries not found"}),404

@app.route("/api/logout", methods=['POST'])
def logout():
    session.pop('username', None)
    return jsonify({"message": "You're now logged out"}),200

#app.config.from_object(app_config[os.getenv('APP_SETTINGS')])

if __name__=='__main__':
    connection_to_database = DbConnection()
    connection_to_database.create_users_table()
    connection_to_database.create_diary_table()
    app.run()
