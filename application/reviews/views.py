from application import app, db
from flask import redirect, render_template, request, url_for
from application.reviews.models import Review, Author, Book

@app.route("/reviews", methods=["GET"])
def reviews_index():
    return render_template("reviews/list.html", reviews = db.session.query(Author.name, Book.book_name, Review.review, Review.stars, Review.id).\
            filter(Review.book_id == Book.id).\
            filter(Book.author_id == Author.id).\
            group_by(Review.id).all())

@app.route("/reviews/new/")
def reviews_form():
    return render_template("reviews/new.html")

@app.route("/reviews/<review_id>/", methods=["POST"])
def reviews_modify(review_id):
    r = Review.query.get(review_id)
    r.review = ""
    db.session().commit()

    return redirect(url_for("reviews_index"))

@app.route("/reviews/", methods=["POST"])
def reviews_create():

    if db.session.query(Author).filter(Author.name == request.form.get("author")).scalar() is None:
        a = Author(request.form.get("author"))
        db.session.add(a)
        db.session.commit()

    if db.session.query(Book).filter(Book.book_name == request.form.get("book")).scalar() is None:
        a = db.session.query(Author.id).filter(Author.name == request.form.get("author")).scalar()
        b = Book(request.form.get("book"), a)
        db.session.add(b)
        db.session.commit()

    b = db.session.query(Book.id).filter(Book.book_name == request.form.get("book")).scalar()
    r = Review(b, request.form.get("review"), request.form.get("stars"))

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reviews_index"))
