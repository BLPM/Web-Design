from flask_login import UserMixin
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model,UserMixin):
    __tablename__ = 'user'
    #
    id = db.Column(db.Integer, primary_key=True)
    #
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())

    confirmed_at = db.Column(db.DateTime())

    roles = db.relationship('Role', secondary='roles_users',
                         backref=db.backref('users', lazy='dynamic'))

    def role(self):
        for item in self.roles:
            return item.name
    def name(self):
        return self.name


class Article(db.Model):
    __tablename__ = 'Article'
    id = db.Column(db.Integer(), primary_key=True)
    PublisherID=db.Column('PublisherID', db.Integer(),db.ForeignKey('user.id'))
    
    title = db.Column(db.String(80), unique=False)
    Summary = db.Column(db.String(255))
    Content = db.Column(db.String(1000))



