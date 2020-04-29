from application import db
from application.models import Base
from application.auth.models import User
from application.reviews.models import Author, Book, Review
from sqlalchemy.sql import text

class MustReads(Base):

    __tablename__ = "mustreads"

    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable = False)
    read = db.Column(db.Boolean, nullable=False)

    def __init__(self, book_id):
        self.book_id = book_id

    @staticmethod
    def get_read(boolean, id):
        stmt = text("SELECT Mustreads.id, Author.name, Book.book_name, Review.id "
                    "FROM Mustreads LEFT JOIN Book ON Mustreads.book_id = Book.id "
                    "LEFT JOIN Author ON Book.author_id = Author.id "
                    "LEFT JOIN Review ON Mustreads.book_id = Review.book_id "
                    "WHERE Mustreads.read = :boolean AND Mustreads.account_id = :id "
                    "GROUP BY Mustreads.id, Author.name, Book.book_name, Review.id").params(boolean = boolean, id = id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "author":row[1], "book":row[2], "review":row[3]})

        return response