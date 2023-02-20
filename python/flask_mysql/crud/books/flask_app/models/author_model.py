from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book_model import Book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Create New Author
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO authors(name)
                VALUE (%(name)s);
                """
        result = connectToMySQL('books_schema').query_db(query, data)
        return result

    #Get All Authors
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM authors;
                """
        result = connectToMySQL('books_schema').query_db(query)
        author_instances = []
        for row in result:
            this_author = cls(row)
            author_instances.append(this_author)
        return author_instances

    #Get One Author
    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * 
                FROM authors
                LEFT JOIN favorites
                ON authors.id = favorites.author_id
                LEFT JOIN books
                ON favorites.book_id = books.id
                WHERE authors.id = %(id)s;
                """
        result = connectToMySQL('books_schema').query_db(query, data)
        if result:
            this_author = cls(result[0])
            these_books = []
            for row in result:
                book_dict = {
                    'id': row['books.id'],
                    'title': row['title'],
                    'num_of_pages': row['num_of_pages'],
                    'created_at': row['books.created_at'],
                    'updated_at': row['books.updated_at']
                }
                this_book = Book(book_dict)
                these_books.append(this_book)
                this_author.books = these_books
                return this_author
            return False
