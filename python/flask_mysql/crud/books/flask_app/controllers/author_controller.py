from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

#Author Render
@app.route('/')
def author_home():
    author_list = Author.get_all()
    return render_template("authors.html", author_list=author_list)

#Author Capture
@app.route('/process', methods = ['POST'])
def capture_author():
    session['name'] = request.form['name']
    new_author = Author.create(request.form)
    return redirect(f"/authors/{new_author}")

#Author Favorite Book
@app.route('/authors/<int:id>')
def authors_books(id):
    data = {'id': id}
    authors_books = Author.get_one(data)
    return render_template("author_favorite.html", authors_books = authors_books)

#Book Capture
@app.route('/processbook', methods = ['POST'])
def capture_authors_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")