import email
from flask import Flask, render_template, flash
from forms import UserForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = "e07e5ecdb25b94b71947500f166ce38e"

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return '<Name %r>' % self.name


@app.route("/")
@app.route("/home")
def index():
    anime_list = ["Attack on Titan", "Steins;Gate", "Fate Series"]
    return render_template('index.html', anime_list=anime_list)


@app.route("/users/add", methods=['GET', 'POST'])
def users():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        form.name.data = ''
        form.email.data = ''
        our_users = Users.query.order_by(Users.date_added)
        flash(f"User {name} submitted successfully!")
        return render_template('user.html', name=name, form=form, our_users=our_users)
    return render_template('user.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True)
