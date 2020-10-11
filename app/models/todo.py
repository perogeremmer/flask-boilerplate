from app import db
from datetime import datetime

from app.models.user import Users


class Todos(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey(Users.id), nullable=True)
    parent_id = db.Column(db.String(36), db.ForeignKey(id), nullable=True)
    title = db.Column(db.String(230), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    finished_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_detail = db.relationship("Users", backref="user_detail_todo")
    parent = db.relationship('Todos', remote_side=id, backref='parent_detail_todo')
    children = db.relationship('Todos', foreign_keys=parent_id)

    def __repr__(self):
        return '<Todo {}>'.format(self.id)
