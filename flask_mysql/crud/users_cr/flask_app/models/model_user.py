# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'users'

class User:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database

    #C
    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        # returns ID of newly created record
        return connectToMySQL(DATABASE).query_db(query, data)

    #R
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    #U
    #D