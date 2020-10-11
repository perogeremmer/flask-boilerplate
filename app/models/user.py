from app import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(200), index=True, unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.name)