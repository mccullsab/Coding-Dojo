from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model, destination_model

class Blog:
    def __init__(self, data):
        self.id = data['id']
        self.rating = data['rating']
        self.memory = data['memory']
        self.image = data['image']
        self.created_at = data['created_at']
        self.created_at = data['updated_at']
        self.user_id = data['destination_id']

#_________________Create a blog_______________
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO blogs(rating,memory, destination_id)
                VALUES (%(rating)s, %(memory)s, %(destination_id)s);
                """
        results = connectToMySQL('project_one').query_db(query, data)
        return results

#_________________Get All blogs_______________
    @classmethod
    def get_all(cls):
        query = """
                SELECT *
                FROM blogs
                LEFT JOIN destinations
                ON destinations.id = blogs.destination_id
                LEFT JOIN users
                ON users.id = destinations.user_id;
                """
        results = connectToMySQL('project_one').query_db(query)
        blog_instances = []
        for row in results:
            this_blog = cls(row)
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            destination_data = {
                **row,
                'id': row['destinations.id'],
                'created_at': row['destinations.created_at'],
                'updated_at': row['destinations.updated_at']
            }
            this_user = user_model.User(user_data)
            this_destination = destination_model.Destination(destination_data)
            this_blog.traveller = this_user
            this_blog.destination = this_destination
            blog_instances.append(this_blog)
            # print("!!!!\n\n",blog_instances)
        return blog_instances

#_________________Get All blogs - one user_______________
    @classmethod
    def get_all_one_user(cls, data):
        query = """
                SELECT *
                FROM blogs
                LEFT JOIN destinations
                ON destinations.id = blogs.destination_id
                LEFT JOIN users
                ON users.id = destinations.user_id
                WHERE users.id = %(id)s;
                """
        results = connectToMySQL('project_one').query_db(query, data)
        blog_instances = []
        for row in results:
            this_blog = cls(row)
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            destination_data = {
                **row,
                'id': row['destinations.id'],
                'created_at': row['destinations.created_at'],
                'updated_at': row['destinations.updated_at']
            }
            this_user = user_model.User(user_data)
            this_destination = destination_model.Destination(destination_data)
            this_blog.traveller = this_user
            this_blog.destination = this_destination
            blog_instances.append(this_blog)
        return blog_instances

#_________________Get All blogs - one destination_______________
    @classmethod
    def get_all_one_destination(cls, data):
        query = """
                SELECT *
                FROM blogs
                LEFT JOIN destinations
                ON destinations.id = blogs.destination_id
                LEFT JOIN users
                ON users.id = destinations.user_id
                WHERE destinations.id = %(id)s;
                """
        results = connectToMySQL('project_one').query_db(query, data)
        print("!!!!!!!!!!!!!!!\n\n\n!!!!!!!!!!!!!!!!!!", results)
        blog_instances = []
        for row in results:
            this_blog = cls(row)
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            destination_data = {
                **row,
                'id': row['destinations.id'],
                'created_at': row['destinations.created_at'],
                'updated_at': row['destinations.updated_at']
            }
            this_user = user_model.User(user_data)
            this_destination = destination_model.Destination(destination_data)
            this_blog.traveller = this_user
            this_blog.destination = this_destination
            blog_instances.append(this_blog)
        return blog_instances
    
#______________________Get One Blog______________
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM blogs
                LEFT JOIN destinations
                ON destinations.id = blogs.destination_id
                LEFT JOIN users
                ON users.id = destinations.user_id
                WHERE blogs.id = %(id)s;
                """
        results = connectToMySQL('project_one').query_db(query, data)
        if results:
            this_blog = cls(results[0])
            row = results[0]
            user_data = {
                **row,
                'id' : row['users.id'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.created_at']
            }
            this_user = user_model.User(user_data)
            this_blog.traveller = this_user
            return this_blog
        return False
    
# ___________________Validate a Blog________________

    @staticmethod
    def validate(form_data):
        is_valid = True
        if len(form_data['rating']) < 1:
            flash("must have a rating.")
            is_valid = False
        return is_valid