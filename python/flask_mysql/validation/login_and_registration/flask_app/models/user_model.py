from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #Create
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO users(first_name,last_name,email,password)
                VALUES (%(first_name)s, %(last_name)s,%(email)s, %(password)s);
                """
        results = connectToMySQL('login_register_schema').query_db(query, data)
        return results

    #Get One
    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM users
                WHERE id = %(id)s;
                """
        results = connectToMySQL('login_register_schema').query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def get_by_email(cls, data):
        query = """
                SELECT * FROM users
                WHERE users.email = %(email)s;
                """
        results = connectToMySQL('login_register_schema').query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
    #Validate
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if len(data['email']) < 1:
            flash("Email too short.")
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        else:
            data_for_email = {
                'email': data['email']
            }
            potential_user = User.get_by_email(data_for_email)
            if potential_user:
                is_valid = False
                flash("email already taken!")
        if len(data['password']) < 8:
            flash("password must be at least 8 characters.")
            is_valid = False
        elif not data['password'] == data['confirm_password']:
            is_valid = False
            flash("passwords don't match!")
        return is_valid
