from application import app, db
from flask import redirect, render_template, request, url_for
from application.reviews.models import Review, Author, Book

@app.route("/reviews", methods=["GET"])
def reviews_index():
    return render_template("reviews/list.html", reviews = Review.query.all())

@app.route("/reviews/new/")
def reviews_form():
    return render_template("reviews/new.html")

@app.route("/reviews/", methods=["POST"])
def reviews_create():

    if Author.query.get(request.form.get("author")) is None:
        a = Author(request.form.get("author"))
        db.session.add(a)
        db.session.commit()

    if Book.query.get(request.form.get("book")) is None:
        a = Author.query.get(request.form.get("author"))
        b = Book(request.form.get("book"), a.id)
        db.session.add(b)
        db.session.commit()

    b = Book.query.get(request.form.get("book"))
    r = Review(request.form.get("review"), request.form.get("stars"), b.id)

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reviews_index"))
