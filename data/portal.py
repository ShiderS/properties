import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class Portal(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'portals'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    assigned_by = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    inn = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tag = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    def set_inn(self, inn):
        self.inn = generate_password_hash(inn)

    def check_inn(self, inn):
        return check_password_hash(self.hashed_inn, inn)