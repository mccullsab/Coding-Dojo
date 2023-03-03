from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.blog_model import Blog
from flask_app.models.user_model import User
from flask_app.models.destination_model import Destination

from flask import flash

# -------------Render - Create a blog-------------


@app.route('/blog/create/<int:id>')
def new_blog(id):
    data = {
        'id': session['user_id']
    }
    logged_user = User.get_one(data)
    destination_info =  Destination.get_by_id({'id': id})
    print("!!!!!!!!!!!!!\n\n\n", destination_info.memory_start_date)
    return render_template("trip_new.html", logged_user=logged_user, destination_info = destination_info)


# ---------------Create a Blog-------------------

@app.route('/create/blog/<int:id>', methods=["POST"])
def create_blog(id):
    print(request.form)
    if not Blog.validate(request.form):
        return redirect('/blog/create')
    blog_data = {
        **request.form,
        'user_id': session['user_id'],
        'destination_id': id
    }
    Blog.create(blog_data)
    return redirect('/dashboard')

#-----------RENDER ALL-----EDIT------

@app.route('/trip/view')
def view_all():
    data = {
        'id' : session['user_id']
    }
    blog_instances = Blog.get_all()
    # Aggregate blogs by location
    # this is a dictionary of location: (sum rating, count ratings)
    aggregated_blogs = {}
    for blog in blog_instances:
        loc = blog.destination.location
        if loc not in aggregated_blogs:
            aggregated_blogs[loc] = (blog.rating, 1)
        else:
            sum_rating, count_rating = aggregated_blogs[loc]
            aggregated_blogs[loc] = (sum_rating + blog.rating, count_rating+1)
    
    # convert back to array
    blog_instances = []
    for loc, (sum_rating, count_rating) in aggregated_blogs.items():
        blog_instances.append({'location': loc, 'rating': sum_rating / count_rating})

    logged_user = User.get_one(data)
    # destination_instances = Destination.get_all()
    return render_template('trip_showall.html', blog_instances=blog_instances)

#calculate dates, pass into jinja, use variable in a for loop,


