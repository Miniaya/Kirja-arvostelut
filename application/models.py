from application import db

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default = db.func.current_timestamp(0))
    date_modified = db.Column(db.DateTime, default = db.func.current_timestamp(0),
        onupdate = db.func.current_timestamp(0))