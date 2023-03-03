from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model, blog_model, destination_model


class Destination:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.memory_start_date = data['memory_start_date']
        self.memory_end_date = data['memory_end_date']
        self.created_at = data['created_at']
        self.created_at = data['updated_at']
        self.user_id = data['user_id']

#_________________Create a destination_______________
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO destinations(location,memory_start_date, user_id)
                VALUES (%(location)s, %(memory_start_date)s, %(user_id)s);
                """
        results = connectToMySQL('project_one').query_db(query, data)
        return results
    
#______________________Get All Blogs - One Destination______________
    @classmethod
    def get_all_blogs(cls, data):
        query = """
                SELECT * FROM destinations
                LEFT JOIN users
                ON users.id = destinations.user_id
                LEFT JOIN blogs
                ON destinations.id = blogs.destination_id
                WHERE destinations.id = %(id)s;
                """
        results = connectToMySQL('project_one').query_db(query, data)
        print("\n\n\n\n", results, "\n\n\n\n")
        blog_instances = []
        for row in results:
            this_destination = cls(results[0])
            row = results[0]
            user_data = {
                **row,
                'id' : row['users.id'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.created_at']
            }
            blog_data = {
                **row,
                'id': row['blogs.id'],
                'created_at': row['blogs.created_at'],
                'updated_at': row['blogs.updated_at']
            }
            this_user = user_model.User(user_data)
            this_blog = blog_model.Blog(blog_data)

            this_destination.traveller = this_user
            this_destination.blog = this_blog

            blog_instances.append(this_destination)
        # this_destination.blogs = blog_instances
    
        return this_destination

#_________________Get All blogs - one user_______________
    @classmethod
    def get_all_one_user(cls, data):
        query = """
                SELECT *
                FROM destinations
                LEFT JOIN blogs
                ON destinations.id = blogs.destination_id
                LEFT JOIN users
                ON users.id = destinations.user_id
                WHERE users.id = %(id)s;
                """
        results = connectToMySQL('project_one').query_db(query, data)
        # print(results)
        destination_instances = []
        for row in results:
            this_destination = cls(row)
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            blog_data = {
                **row,
                'id': row['blogs.id'],
                'created_at': row['blogs.created_at'],
                'updated_at': row['blogs.updated_at']
            }
            this_user = user_model.User(user_data)
            this_destination = destination_model.Destination(blog_data)
            this_destination.traveller = this_user
            this_destination.destination = this_destination
            destination_instances.append(this_destination)
        return destination_instances

#______________________Get One Destination______________
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM destinations
                LEFT JOIN blogs
                ON destinations.id = blogs.destination_id
                LEFT JOIN users
                ON users.id = destinations.user_id
                WHERE destinations.id = %(id)s;
                """
        results = connectToMySQL('project_one').query_db(query, data)
        if results:
            this_destination = cls(results[0])
            row = results[0]
            user_data = {
                **row,
                'id' : row['users.id'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.created_at']
            }
            this_user = user_model.User(user_data)
            this_destination.traveller = this_user
            return this_destination
        return False

# ___________________Validate a Destination________________

    @staticmethod
    def validate(form_data):
        is_valid = True
        if len(form_data['location']) < 1:
            flash("must have a location.")
            is_valid = False
        if len(form_data['memory_start_date']) < 1:
            flash("must have a start date.")
            is_valid = False
        return is_valid