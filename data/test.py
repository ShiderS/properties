import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Test(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'tests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    titles = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    linked_to = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey("portals.id"),
                                  nullable=False)

