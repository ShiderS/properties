import sqlalchemy
import datetime
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class TestResult(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'test_results'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    id_user = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"),
                                nullable=False)

    id_test = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("tests.id"),
                                nullable=False)

    result = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)