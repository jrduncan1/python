# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojos_and_ninjas'

class Dojo:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # Now we use class methods to query our database

    #C
    @classmethod
    def create(cls, data:dict):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        # returns ID of newly created record
        return connectToMySQL(DATABASE).query_db(query, data)

    #R
    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # data type = LIST OF DICTIONARIES
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        # data type = LIST OF 1 DICTIONARY
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    
    @classmethod
    def show_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id  WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            ninjas_in_dojos = {
                'id': row['ninjas.id'],
                'first_name': row['ninjas.first_name'],
                'last_name': row['ninjas.last_name'],
                'age': row['ninjas.age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(dojo.ninjas_in_dojos)
        return dojo
