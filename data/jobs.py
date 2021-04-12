import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from forms.jobs import JobsForm, AddressJob, Ready


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    employer = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    description = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    info = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.String)
    coords = sqlalchemy.Column(sqlalchemy.String)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    employee = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    user = orm.relation('User')
