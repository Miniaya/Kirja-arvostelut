from application import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default = db.func.current_timestamp())

    user_id = db.Column(db.Integer, nullable = False)
    book_id = db.Column(db.Integer, nullable = False)
    review = db.Column(db.String(144), nullable = False)
    stars = db.Column(db.Integer, nullable = False)

    def __init__(self, review, stars, book_id):
        self.user_id = 1
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
    name = db.Column(db.String(144), nullable = False)

    def __init__(self, name, author_id):
        self.name = name
        self.author_id = author_id