from flask_app import app
from flask_app.models.users_model import Users


### READ ALL - RENDER / VIEW
@app.route('/')
def index():
    all_users = Users.get_all()
    return render_template('index.html', all_users = all_users)

### CREATE user - RENDER
#/table_name/id/action
@app.route('/users/new')
def new_user():
    return render_template ("user_new.html")

###CREATE capture
@app.route("/users/create")
def create_user():
    # print("******************************")
    # print(request.form)
    user_id = Users.create(request.form)
    return redirect(f"/users/{user_id}/show")
    #NEVER RENDER ON A POST

#SHOW/ READ ONE RENDER
@app.route("/users/<int:id>/show")
def show_user(id):
    data = {
        'id': id
    }
    this_user = Users.get_one(data)
    return render_template("user_show.html", this_user = this_user)

#DELETE
@app.route("/users/<int:id>/delete")
def delete(id):
    Users.delete_one({'id': id})
    return redirect('/')

#UPDATE - RENDER
@app.route('/users/<int:id>/edit')
def edit_user(id):
    this_user = Users.get_one({'id': id})
    return render_template("user_edit.html", this_user = this_user)

#UPDATE - Capture
@app.route('/users/<int:id>/update', methods = ['POST'])
def update_user(id):
    print(request.form)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    Users.update(data)
    return redirect('/')