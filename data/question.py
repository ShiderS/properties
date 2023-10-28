import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Question(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'questions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    linked_to = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey("tests.id"),
                                  nullable=False)
    answer = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    qtype = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    answer_var = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("answer_variants.id"),
                                   nullable=True)
