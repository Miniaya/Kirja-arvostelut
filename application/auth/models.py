from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(100), nullable = False)
    username = db.Column(db.String(24), nullable = False)
    password = db.Column(db.String(16), nullable = False)

    reviews = db.relationship("Review", backref='account', lazy = True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["NORMAL"]