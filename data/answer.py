import sqlalchemy
import datetime
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Answer(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'answers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    id_user = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"),
                                nullable=False)

    id_question = sqlalchemy.Column(sqlalchemy.String,
                                    sqlalchemy.ForeignKey("questions.id"),
                                    nullable=False)

    answer = sqlalchemy.Column(sqlalchemy.String,
                               nullable=False)
