import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class AnswerVariant(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'answer_variants'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    var1 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    var2 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    var3 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
