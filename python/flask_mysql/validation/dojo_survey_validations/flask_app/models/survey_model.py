from flask_app.config.mysqlconnection import connectToMySQL

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.id = data['location']
        self.id = data['language']
        self.id = data['comment']
        self.id = data['created_at']
        self.id = data['updated_at']
    
    @classmethod

    
    @staticmethod
