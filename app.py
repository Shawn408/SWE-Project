from enum import unique
import os
import re
import random
import flask
from flask import Flask, render_template
from flask_login import (
    LoginManager,
    UserMixin,
    login_required,
    login_user,
    logout_user,
    current_user,
)
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from tmdb import get_movie_info
from wiki import wiki_link_search

app = flask.Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

load_dotenv(find_dotenv())

bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

url = os.getenv("DATABASE_URL")
if url.startswith("postgres://"):
    url = url.replace("postgres://", "postgresql://", 1)

app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Account(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(1000), nullable=False)


db.create_all()

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return flask.redirect("/")


@app.route("/", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        data = flask.request.form
        user = Account.query.filter_by(username=data["username"]).first()
        if user:
            login_user(user)
            return flask.redirect(flask.url_for("index"))
        else:
            return flask.redirect(flask.url_for("signup"))

    return render_template("login.html")


@app.route("/main", methods=["GET", "POST"])
@login_required
def index():
    user = Account.query.all()
    if not user:
        flask.redirect(flask.url_for("login"))
    else:

        movie_id_query = ["546554", "4232", "423108", "580489", "460465"]

        movie_data = get_movie_info(random.choice(movie_id_query))
        title_search = wiki_link_search(movie_data["title"])

        if flask.request.method == "POST":
            data = flask.request.form
            new_review = Review(
                username=current_user.username,
                movie_id=data["movie_id"],
                rating=data["rating"],
                comment=data["comment"],
            )
            db.session.add(new_review)
            db.session.commit()

        global reviews
        reviews = Review.query.all()
        global num_reviews
        num_reviews = len(reviews)

        return render_template(
            "main.html",
            movie_id=movie_data["movie_id"],
            title=movie_data["title"],
            tagline=movie_data["tagline"],
            genre=movie_data["genre"],
            site=random.choice(movie_data["site"]),
            image=movie_data["baseurl"] + "w500" + movie_data["image"],
            title_search=title_search,
            reviews=reviews,
            num_reviews=num_reviews,
        )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        data = flask.request.form
        u = Account.query.filter_by(username=data["username"]).first()
        if u is None:
            user = Account(username=data["username"])
            db.session.add(user)
            db.session.commit()
            return flask.redirect(flask.url_for("login"))
    return render_template("signup.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return flask.redirect(("/"))


@bp.route("/reviews", methods=["GET", "POST"])
@login_required
def index():
    return flask.render_template("index.html")


@app.route("/edit", methods=["GET", "POST"])
@login_required
def edit():
    current_account = current_user.username
    reviewLog = Review.query.filter_by(username=current_account).all()
    reviewList = []
    for i in reviewLog:
        reviewDict = {}
        reviewDict["id"] = i.id
        reviewDict["movie_id"] = i.movie_id
        reviewDict["rating"] = i.rating
        reviewDict["comment"] = i.comment
        reviewList.append(reviewDict)
    return flask.jsonify({"review": reviewList})


@app.route("/save", methods=["GET", "POST"])
@login_required
def save():
    if flask.request.method == "POST":
        Review.query.filter_by(username=current_user.username).delete()
        db.session.commit()
        stateData = flask.request.json
        for i in stateData:
            movie_id = i["movie_id"]
            rating = i["rating"]
            comment = i["comment"]
            db.session.add(
                Review(
                    username=current_user.username,
                    movie_id=movie_id,
                    rating=rating,
                    comment=comment,
                )
            )
            db.session.commit()
    return flask.redirect(flask.url_for("index"))


app.register_blueprint(bp)

app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
