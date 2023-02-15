# import the function that will return an instance of a connection
# from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
# class Friend:
#     def __init__( self , data ):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.occupation = data['occupation']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
# # Now we use class methods to query our database
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM friends;"
#         # make sure to call the connectToMySQL function with the schema you are targeting.
#         results = connectToMySQL('friends_schema').query_db(query)
#         # Create an empty list to append our instances of friends
#         friends = []
#         # Iterate over the db results and create instances of friends with cls.
#         for friend in results:
#             friends.append( cls(friend) )
#         return friends
    
#     @classmethod
#     def save(cls, data ):
#         query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
#         # data is a dictionary that will be passed into the save method from server.py
#         return connectToMySQL('first_flask').query_db( query, data )   

## COPIED CODE ABOVE

from mysqlconnection import connectToMySQL


class Friend:
    DB = "friends_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.first_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO friends (first_name, last_name, occupation)
                    VALUES (%(first_name)s,%(last_name)s,%(occ)s);"""
        result = connectToMySQL(cls.DB).query_db(query.data)
        return result
#READ
    @classmethod
    def get_one(cls, id):
        query = """SELECT * FROM friends 
                    WHERE id = $(id)s"""
        results = connectToMySQL(cls.DB).query_db(query, {"id":id})
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_friends = []
        for row in results:
            all_friends.append(cls(row))
        return results

    @classmethod
    def update(cls,data):
        query = """UPDATE friends 
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s 
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def delete(cls, friend_id):
        query  = "DELETE FROM friends WHERE id = %(id)s};"
        data = {"id": friend_id}
        return connectToMySQL(cls.DB).query_db(query, data)