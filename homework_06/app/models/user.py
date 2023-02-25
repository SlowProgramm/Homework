from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String

from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class UserModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(35), nullable=False, unique=True, default="default", server_default="default")
    age = Column(Integer(), nullable=True, unique=False)
    address = Column(String(35), nullable=True, unique=False, default="default", server_default="default")
    if TYPE_CHECKING:
        query: Query
