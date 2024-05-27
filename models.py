from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(), default=func.now())
    updated_at = db.Column(db.DateTime(), default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"Task {self.id}: {self.description}"
