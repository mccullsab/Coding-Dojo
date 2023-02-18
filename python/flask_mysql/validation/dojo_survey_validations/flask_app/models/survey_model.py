from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO survey_response(name, location, language, comment)
                VALUES (%(name)s, %(location)s, %(location)s, %(comment)s);
                """
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return results
    
    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM survey_response
                WHERE id = %(id)s;
                """
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        if results:
            this_survey = cls(results[0])
            return this_survey
        return False

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 1:
            flash("Name must be at least 1 character.")
            is_valid = False
        if len(data['location']) < 1:
            flash("location must be selected.")
            is_valid = False
        if len(data['language']) < 1:
            flash("language must be selected.")
            is_valid = False
        if len(data['comment']) < 1:
            flash("comment required.")
            is_valid = False
        return is_valid
