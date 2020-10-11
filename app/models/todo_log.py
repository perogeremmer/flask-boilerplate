from app import db
from datetime import datetime

from app.models.todo import Todos
from app.models.user import Users


class TodoLogs(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey(Users.id), nullable=True)
    todo_id = db.Column(db.String(36), db.ForeignKey(Todos.id), nullable=True)
    message = db.Column(db.Text())
    type = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_detail = db.relationship("Users", backref="user_detail_todo_logs")
    todo_detail = db.relationship("Todos", backref="todo_detail_todo_logs")

    def __repr__(self):
        return '<TodoLogs {}>'.format(self.id)
