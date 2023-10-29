import sqlalchemy
import datetime
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class PortalRight(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'portal_rights'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    id_user = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"),
                                nullable=False)

    id_portal = sqlalchemy.Column(sqlalchemy.String,
                                  sqlalchemy.ForeignKey("portals.id"),
                                  nullable=False)

    type = sqlalchemy.Column(sqlalchemy.String,
                             nullable=False)
