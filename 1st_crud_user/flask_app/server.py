from flask import Flask, render_template, redirect, request
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("read.html", users = User.show_all())

@app.route('/add')
def add():
    return render_template("create.html")

@app.route('/create', methods = ["POST"])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/user/<int:id>')
def user(id):
    data = {
        "id" : id
    }
    return render_template("read_one.html", user = User.get_one(data))

@app.route('/edit/user/<int:id>')
def edit_page(id):
    data = {
        "id" : id
    }
    return render_template("edit.html", user = User.get_one(data))

@app.route('/edit/user', methods = ["POST"])
def edit_user():
    User.update(request.form)
    return redirect('/users')

@app.route('/delete/user/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/users')



if __name__ == "__main__":
    app.run(port=8000, debug = True)
