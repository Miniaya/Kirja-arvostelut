from application import db
from application.models import Base
from application.auth.models import User
from sqlalchemy.sql import text

class Review(Base):

    __tablename__ = "review"
    
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable = False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable = False)
    review = db.Column(db.String(400), nullable = False)
    stars = db.Column(db.Integer, nullable = False)

    def __init__(self, book_id, review, stars):
        self.book_id = book_id
        self.review = review
        self.stars = stars

    @staticmethod
    def get_review(id=1):
        stmt = text("SELECT Author.name, Book.book_name, Review.review, Review.stars, Account.username, Review.date_modified, Review.id "
                    "FROM Review LEFT JOIN Book ON Review.book_id = Book.id "
                    "LEFT JOIN Author ON Book.author_id = Author.id "
                    "LEFT JOIN Account ON Review.account_id = Account.id "
                    "WHERE Review.account_id = :id "
                    "GROUP BY Review.id, Author.name, Book.book_name, Account.username "
                    "ORDER BY Review.date_modified DESC").params(id = id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"author":row[0], "book":row[1], "review":row[2], "stars":row[3], "username":row[4], "date":row[5], "id":row[6]})
        
        return response

    @staticmethod
    def get_all_reviews():
        stmt = text("SELECT Author.name, Book.book_name, Review.review, Review.stars, Account.username, Review.date_modified, Review.id "
                    "FROM Review LEFT JOIN Book ON Review.book_id = Book.id "
                    "LEFT JOIN Author ON Book.author_id = Author.id "
                    "LEFT JOIN Account ON Review.account_id = Account.id "
                    "GROUP BY Review.id, Author.name, Book.book_name, Account.username "
                    "ORDER BY Review.date_modified DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"author":row[0], "book":row[1], "review":row[2], "stars":row[3], "username":row[4], "date":row[5], "id":row[6]})
        
        return response

    @staticmethod
    def find_by_author(auth):
        stmt = text("SELECT Author.name, Book.book_name, Review.review, Review.stars, Account.username, Review.date_modified, Review.id "
                    "FROM Review LEFT JOIN Book ON Review.book_id = Book.id "
                    "LEFT JOIN Author ON Book.author_id = Author.id "
                    "LEFT JOIN Account ON Review.account_id = Account.id "
                    "WHERE LOWER(Author.name) LIKE :auth "
                    "GROUP BY Review.id, Author.name, Book.book_name, Account.username "
                    "ORDER BY Review.date_modified DESC").params(auth = '%' + auth + '%')
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"author":row[0], "book":row[1], "review":row[2], "stars":row[3], "username":row[4], "date":row[5], "id":row[6]})

        return response

class Author(db.Model):

    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(144), nullable = False)

    books = db.relationship("Book", backref="author", lazy=True)

    def __init__(self, name):
        self.name = name

class Book(db.Model):

    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable = False)
    book_name = db.Column(db.String(144), nullable = False)

    reviews = db.relationship("Review", backref="book", lazy=True)

    def __init__(self, name, author_id):
        self.book_name = name
        self.author_id = author_id
