from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #READALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        print(results)
        user_instances = []
        if results:
            for row in results:
                this_user = cls(row)
                user_instances.append(this_user)
        return user_instances
    
    #CREATE
    @classmethod
    def create(cls, data):
        print(data)
        query = """
        INSERT INTO users(first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        result = connectToMySQL('users_schema').query_db(query, data)
        return result
    
    #READ ONE
    @classmethod
    def get_one(cls, data):
        query = """
            SELECT * FROM users
            WHERE id = %(id)s
        """
        result = connectToMySQL('users_schema').query_db(query, data)
        print(result)
        if result:
            this_user = cls(result[0])
            return this_user
        return False
    
    #UPDATE
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s,
            last_name = %(last_name)s,
            email = %(email)s
        WHERE id = %(id)s
        """
        return connectToMySQL('users_schema').query_db(query, data)
    
    #DELETE
    @classmethod
    def delete_one(cls, data):
        query = """
            DELETE FROM users
            WHERE id = %(id)s;
        """
        return connectToMySQL('users_schema').query_db(query, data)