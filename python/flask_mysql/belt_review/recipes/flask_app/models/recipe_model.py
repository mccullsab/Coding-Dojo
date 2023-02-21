from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app.models import user_model


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_thirty = data['under_thirty']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #Create
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO recipes(name,description,instructions,date_made,under_thirty,user_id)
                VALUES (%(name)s, %(description)s,%(instructions)s, %(date_made)s, %(under_thirty)s,%(user_id)s);
                """
        results = connectToMySQL('recipes').query_db(query, data)
        return results     
    
    #Get all Recipes
    @classmethod
    def get_all(cls):
        query = """
                SELECT * 
                FROM recipes
                LEFT JOIN users
                ON users.id = recipes.user_id;
                """
        results = connectToMySQL('recipes').query_db(query)
        # print("!!!!!!!!!!!!$$$$$", results)
        recipe_instances = []
        for row in results:
            this_recipe = cls(row)
            # recipe_instances.append(this_recipe)
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            this_user = user_model.User(user_data)
            this_recipe.poster = this_user
            recipe_instances.append(this_recipe)
        return recipe_instances 
    
    #Read ONE
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM recipes
                JOIN users
                ON users.id = recipes.user_id
                WHERE users.id = %(id)s;
                """
        results = connectToMySQL('recipes').query_db(query, data)
        print("#################",results)
        if results:
            this_recipe = cls(results[0])
            row = results[0]
            user_data = {
                **row,
                'id' : row['users.id'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.created_at']
            }
            this_user = user_model.User(user_data)
            this_recipe.poster = this_user
            return this_recipe

    #Update
    @classmethod
    def update(cls, data):
        query = """
                UPDATE recipes
                SET
                name = %(name)s,
                description = %(description)s,
                instructions = %(instructions)s,
                date_made = %(date_made)s,
                under_thirty = %(under_thirty)s
                WHERE id = %(id)s;
                """
        results = connectToMySQL('recipes').query_db(query, data)
        return results

    #DELETE
    @classmethod
    def delete(cls, data):
        query="""
            DELETE FROM recipes
            WHERE id = %(id)s;
            """
        results = connectToMySQL('recipes').query_db(query, data)
        return results


    #Validate
    @staticmethod
    def validate(form_data):
        is_valid = True
        if len(form_data['name']) < 1:
            flash("name must be at least 1 character.")
            is_valid = False
        if len(form_data['date_made']) < 1:
            flash("must have a date.")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("must have a description.")
            is_valid = False
        if len(form_data['instructions']) < 1:
            flash("must have instructions.")
            is_valid = False
        if 'under_thirty' not in form_data:
            is_valid = False
            flash("under_thirty is required.")
        return is_valid
        
