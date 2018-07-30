from flask import jsonify

class DbConnection:
    print("############ GENERATING SCHEMA ##################")
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname = 'andelabootcamp'\
            user='postgres' host='localhost' password='5ure5t@re!' port='5432'")
            self.connection.autocommit = True
            seldeff.cursor = self.connection.cursor()
        except Exception as e:
            print("############ FAILED TO GENERATE SCHEMA ##################")
            return jsonify({"Error Message": e.message} )
            exit()


    def create_users_table(self):
        users_table_command = "CREATE TABLE IF NOT EXISTS users(\
          uid serial PRIMARY KEY,\
          firstname VARCHAR(50) not null,\
          lastname VARCHAR(50) not null,\
          email VARCHAR(100) not null unique,\
          username VARCHAR(100) not null unique,\
          password VARCHAR(128) not null \
        )"
        self.cursor.execute(users_table_command)
        print "==> Created Users Table"

    def create_diary_table(self):
        diary_table_command = "CREATE TABLE IF NOT EXISTS diary(\
          did serial PRIMARY KEY,\
          username VARCHAR(100) not null,\
          entry TEXT,\
          event_date DATE, \
          entry_date DATE,\
          notification_date DATE,\
          version VARCHAR(100), \
          FOREIGN KEY (username) REFERENCES users(username)\
          ON UPDATE CASCADE ON DELETE RESTRICT\
        )"
        self.cursor.execute(diary_table_command)
        print "==> Created Diaries Table"
        print("############ SCHEMA GENERATED ##################")

class DiryTable(DbConnection):
    def __init__(self, username, entry, event, event_date, notification_date,
    version):
        self.username = username
        self.entry = entry
        self.event = event
        self.event_date = event_date
        self.entry_date = entry_date
        self.notification_date = notification_date
        self.version = version

        diary_table_command = "INSERT INTO diary(username, entry,event_date, \
        entry_date, notification_date, version) VALUES({}, {}, {}, {}, \
        {}, {}, {})".format(username, entry, event_date, notification_date,
        version)
