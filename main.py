
class Registration:
    #These variables are only usable within this class
    #To use theme elsewhere, explicitly include the classname
    __firstname = None
    __lastname = None
    __username = None
    __email = None
    __password = None
    __confirm_password = None
    __version = None

    def __init__(self, firstname, lastname, username, email, password,version):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(password):
        return self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def passwords_match(password, confirm_password):
        return password == confirm_password
    #
    # Setting Properties
    #

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        return self.firstname = value

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        return self.lastname = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        return self.username = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        return self.email = value

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, value):
        return self.version = version

    def serialize(self):
        return {
            "firstname": self.firstname
            "lastname": self.lastname
            "username": self.username
            "email": self.email
            "password": self.password
            "version": self.version
            "id": self.id
        }

    def insert_to_db(self):
         conn = psycopg2.connect(host="localhost",database="andelabootcamp",
         user="postgres", password="5ure5t@re!")


class login:
    #These variables are only usable within this class
    #To use theme elsewhere, explicitly include the classname
    __username = None
    __password = None

    def __init__(self, username, password):
        self.username = username
        self.email = email

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def passwords_match(password, confirm_password):
        return password == confirm_password
    #
    # Setting Properties
    #

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        return self.username = value

    @version.setter
    def version(self, value):
        return self.version = version

    def serialize(self):
        return {
            "message": "logged in successfully"
        }
