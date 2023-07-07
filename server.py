from flask import Flask, render_template, request, redirect

app = Flask(__name__)

from user import User

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("Read.html", all_users = users)

@app.route("/users/new")
def create():

    return render_template("Create.html")

@app.route('/create_form',methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)