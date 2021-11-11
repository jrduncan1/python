import re
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app

bcrypt = Bcrypt(app)

# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE_SCHEMA = 'recipes_schema'

class Recipe:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made_on = data['date_made_on']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # Now we use class methods to query our database

    # CREATE___________________________________________________________
    # create recipte
    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made_on, under_30_min, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made_on)s, %(under_30_min)s, %(user_id)s)"
        # returns the id of the new recipe
        return connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

    # RETRIEVE_________________________________________________________
    @classmethod
    def retrieve_all_recipes(cls, data):
        query = "SELECT * FROM recipes"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

        recipes = []
        for row in results:
            recipes.append(Recipe(row))
        return recipes



    @classmethod
    def retrieve_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE recipes.id = %(id)s"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        if results:
            return Recipe(results[0])
        else:
            return False
    
    # UPDATE____________________________________________________________
    # DELETE____________________________________________________________

    # VALIDATIONS______________________________
    @staticmethod
    def recipe_validate(check_recipe):
        is_valid = True

        if len(check_recipe["name"]) < 3:
            flash("Recipe name must longer than three(3) characters!", "create_name")
            is_valid = False

        if len(check_recipe["description"]) < 3:
            flash("Description must be longer than three(3) characters!", "create_description")
            is_valid = False

        if len(check_recipe["instructions"]) < 3:
            flash("Instructions must be longer than three(3) characters!", "create_instructions")
            is_valid = False

        if len(check_recipe["date_made_on"]) < 1:
            flash("Date made is a required field.", "create_date_made_on")
            is_valid = False
        
        if not "under_30_min" in check_recipe:
            flash("Please select one.", "create_under_30_min")
            is_valid = False

        return is_valid
