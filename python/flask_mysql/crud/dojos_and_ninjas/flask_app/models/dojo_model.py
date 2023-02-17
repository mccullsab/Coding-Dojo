from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    # Render All
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojo_instances = []
        for row in result:
            this_dojo = cls(row)
            dojo_instances.append(this_dojo)
        return dojo_instances
    
    #Create Dojo
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos(name)
                VALUES(%(name)s);
                """
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return result
    
    #Get One
    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM dojos
                LEFT JOIN ninjas
                ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(id)s;
                """
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        print("+++++++++++++++++++", result)
        if result:
            this_dojo = cls(result[0])
            these_ninjas = []
            for row in result:
                ninja_dict = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'dojo_id': row['dojo_id']
                }
                this_ninja = Ninja(ninja_dict)
                these_ninjas.append(this_ninja)
            this_dojo.ninjas = these_ninjas
            return this_dojo
        return False
