from application import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default = db.func.current_timestamp())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
    book_id = db.Column(db.Integer, nullable = False)
    review = db.Column(db.String(144), nullable = False)
    stars = db.Column(db.Integer, nullable = False)

    def __init__(self, book_id, review, stars):
        self.book_id = book_id
        self.review = review
        self.stars = stars

class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(144), nullable = False)

    def __init__(self, name):
        self.name = name

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer, nullable = False)
    book_name = db.Column(db.String(144), nullable = False)

    def __init__(self, name, author_id):
        self.book_name = name
        self.author_id = author_id