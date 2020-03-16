from application import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(144), nullable = False)
    name = db.Column(db.String(144), nullable = False)

    def __init__(self, author, name):
	self.author = author
        self.name = name
