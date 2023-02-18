from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO email(email)
                VALUES (%(email)s);
                """
        results = connectToMySQL('email_valid_schema').query_db(query,data)
        return results
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM email;
                """
        results = connectToMySQL('email_valid_schema').query_db(query)
        emails_instances = []
        for row in results:
            this_email = cls(row)
            emails_instances.append(this_email)
        return emails_instances
    
    @staticmethod
    def validate(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid


