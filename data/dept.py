import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Dept(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'depts'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    linked_to = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey("depts.id"),
                                  nullable=True)
