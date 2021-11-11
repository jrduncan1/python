import re
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app

bcrypt = Bcrypt(app)

# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE_SCHEMA = 'recipes_schema'

class User:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database

    # CREATE___________________________________________________________
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        # returns the id of the new user
        return connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

    # RETRIEVE_________________________________________________________
    @classmethod
    def retrieve_user_with_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        if results:
            return User(results[0])
        else:
            return False

    @classmethod
    def retrieve_user_with_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        if results:
            return User(results[0])
        else:
            return False
    
    # UPDATE____________________________________________________________
    
    # DELETE____________________________________________________________

    # VALIDATIONS______________________________
    @staticmethod
    def registration_validate(check_user):
        is_valid = True

        if len(check_user["first_name"]) < 2:
            flash("First Name must be at least two(2) characters!", "reg_first_name")
            is_valid = False

        if len(check_user["last_name"]) < 2:
            flash("Last Name must be at least two(2) characters!", "reg_last_name")
            is_valid = False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(check_user['email']): 
            flash("Invalid email address!", "reg_email")
            is_valid = False
        else:
            user = User.retrieve_user_with_email({'email': check_user['email']})
            if user:
                flash("Account already exists! Please try logging in or using a different email.")
                is_valid = False

        if len(check_user["password"]) < 8:
            flash("Password must be at least eight(8) characters!", "reg_password")
            is_valid = False

        if check_user["password"] != check_user['confirm_password']:
            flash("Passwords do not match!", "reg_confirm_password")
            is_valid = False
        
        return is_valid
    

    @staticmethod
    def login_validate(check_user):
        user = User.retrieve_user_with_email({"email": check_user['email']})

        if not user:
            flash("Invalid login information.", "reg_invalid_user")
            return False
        
        if not bcrypt.check_password_hash(user.password, check_user['password']):
            flash("Invalid password.", "reg_invalid_password")
            return False
        
        return True