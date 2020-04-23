from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.reviews.models import Author, Book, Review

from application.read.models import MustReads
from application.read.forms import ReadForm

@app.route("/mustread")
@login_required
def read_mustReads():
    return render_template("read/mustread.html", books = MustReads.get_read(0, current_user.id))

@app.route("/readlist", methods=["GET"])
@login_required
def read_listRead():
    return render_template("read/readlist.html", books = MustReads.get_read(1, current_user.id))

@app.route("/read/new/")
@login_required
def read_form():
    return render_template("read/addtolist.html", form = ReadForm())

@app.route("/read/", methods=["POST"])
@login_required
def read_create():
    form = ReadForm(request.form)
    given_author = form.author.data
    given_book = form.name.data

    if not form.validate():
        return render_template("read/addtolist.html", form = form)

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
    r = MustReads(b, form.read.data)
    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()

    if form.read.data:
        return redirect(url_for("read_listRead"))
    else:
        return redirect(url_for("read_mustReads"))