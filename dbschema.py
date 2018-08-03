from flask import jsonify
import psycopg2

conn = psycopg2.connect("dbname = 'andelabootcamp'\
user='postgres' host='localhost' password='5ure5t@re!' port='5432'")
conn.autocommit = True
cur = conn.cursor()


class SchemaGeneration:
    def __init__(self):
        try:
            print("############ GENERATING SCHEMA ##################")
            self.connection = psycopg2.connect("dbname = 'andelabootcamp'\
            user='postgres' host='localhost'\
             password='5ure5t@re!' port='5432'")
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
          password VARCHAR(128) not null \
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

class DiryTable():
    def __init__(self, username, entry, event, event_date, notification_date,
    version):
        self.username = username
        self.entry = entry
        self.event = event
        self.event_date = event_date
        self.entry_date = entry_date
        self.notification_date = notification_date
        self.version = version

        self.connection = psycopg2.connect("dbname = 'andelabootcamp'\
        user='postgres' host='localhost' password='5ure5t@re!' port='5432'")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        diary_table_command = "INSERT INTO diary(username, entry,event_date, \
        entry_date, notification_date, version) VALUES({}, {}, {}, {}, \
        {}, {}, {})".format(username, entry, event_date, notification_date,
        version)

class Registration(SchemaGeneration):
    def __init__(self, firstname, lastname, email,username,password,public_id):
        self.firstname = firstname,
        self.lastname = lastname,
        self.email = email
        self.public_id = public_id
        self.password = password

    def register(self,firstname, lastname, email,username,password,public_id):
        try:

            register_command = "INSERT INTO users(\
              firstname,lastname,email,username,passwordl,\
              public_id) VALUES('{}','{}','{}','{}','{}','{}'))".format(
              firstname, lastname, email,username,password,public_id
              )
            cur.execute(register_command)
            return True
        except Exception as e:
            return jsonify({"Error Message": e.message} )
