# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas'

class Ninja:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    # Now we use class methods to query our database

    #C
    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        # returns ID of newly created record
        return connectToMySQL(DATABASE).query_db(query, data)

    #R
    @classmethod
    def get_one(cls, **data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s"
        # data type = LIST OF 1 DICTIONARY
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
