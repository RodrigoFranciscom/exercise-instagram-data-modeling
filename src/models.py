import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(200), nullable=False)
    lastname = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False, unique=True)

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'))
    user_to_id = Column(Integer, ForeignKey('User.id'))

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    photo_url = Column(String(350), nullable=False )
    post_to_id = Column(Integer, ForeignKey('User.id'))

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False)
    url = Column(String(350), nullable=False)
    post_to_id = Column(Integer, ForeignKey('Post.id'))

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('User.id'))
    comment_text = Column(String(450), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
