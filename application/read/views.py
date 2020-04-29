from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.reviews.models import Author, Book, Review

from application.read.models import MustReads
from application.read.forms import ReadForm

@app.route("/mustread")
@login_required
def read_mustReads():
    return render_template("read/mustread.html", books = MustReads.get_read(False, current_user.id), read = False)

@app.route("/readlist", methods=["GET"])
@login_required
def read_listRead():
    return render_template("read/readlist.html", books = MustReads.get_read(True, current_user.id), read = True)

@app.route("/read/new/")
@login_required
def read_form():
    return render_template("read/addtolist.html", form = ReadForm())

@app.route("/read/delete/<read_id>", methods=["POST"])
@login_required
def read_delete(read_id):
    read = MustReads.query.get(read_id).read
    MustReads.query.filter_by(id=read_id).delete()
    db.session.commit()

    if read == 1:
        return redirect(url_for("read_listRead"))
    else:
        return redirect(url_for("read_mustReads"))

@app.route("/read/<read_id>", methods=["POST"])
@login_required
def read_set_read(read_id):
    r = MustReads.query.get(read_id)
    r.read = True
    db.session.commit()

    return redirect(url_for("read_listRead"))

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
    r = MustReads(b)
    r.read = form.read.data
    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()

    if form.read.data:
        return redirect(url_for("read_listRead"))
    else:
        return redirect(url_for("read_mustReads"))