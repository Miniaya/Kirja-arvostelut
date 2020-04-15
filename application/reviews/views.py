from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.reviews.models import Review, Author, Book
from application.reviews.forms import ReviewForm, SearchForm

@app.route("/frontpage", methods=["GET"])
def reviews_front():
    return render_template("reviews/list.html", reviews = Review.get_all_reviews(), show = 3)

@app.route("/reviews/search", methods=["POST", "GET"])
def reviews_search():
    if request.method == "GET":
        return render_template("reviews/list.html", show = 1, form = SearchForm())

    r = Review.find_by_author(request.form.get("author"))

    return render_template("reviews/list.html", show = 1, reviews = r, form = SearchForm())

@app.route("/reviews", methods=["GET"])
@login_required
def reviews_index():
    return render_template("reviews/list.html", show = 2, reviews = Review.get_review(current_user.id))

@app.route("/reviews/delete/<review_id>", methods=["POST"])
@login_required
def reviews_delete(review_id):
    Review.query.filter_by(id=review_id).delete()
    db.session.commit()

    return redirect(url_for("reviews_index"))

@app.route("/reviews/new/")
@login_required
def reviews_form():
    return render_template("reviews/new.html", form = ReviewForm())

@app.route("/reviews/<review_id>/", methods=["GET", "POST"])
@login_required
def reviews_modify(review_id):
    r = Review.query.get(review_id)

    if request.method == "GET":
        return render_template("reviews/modify.html", review = r)

    r.review = request.form.get("review")
    db.session().commit()

    return redirect(url_for("reviews_index"))

@app.route("/reviews/", methods=["POST"])
@login_required
def reviews_create():
    form = ReviewForm(request.form)
    given_author = form.author.data
    given_book = form.name.data

    if not form.validate():
        return render_template("reviews/new.html", form = form)

    if db.session.query(Author).filter(Author.name == given_author).scalar() is None:
        a = Author(given_author)
        db.session.add(a)
        db.session.commit()

    if db.session.query(Book).filter(Book.book_name == given_book).scalar() is None:
        a = db.session.query(Author.id).filter(Author.name == given_author).scalar()
        b = Book(given_book, a)
        db.session.add(b)
        db.session.commit()

    b = db.session.query(Book.id).filter(Book.book_name == given_book).scalar()
    r = Review(b, form.review.data, form.star.data)
    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reviews_index"))
