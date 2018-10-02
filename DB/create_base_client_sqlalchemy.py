"""
Создание клиентской базы
"""
import datetime
import sys
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Numeric, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///DB/Client.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Contact(Base):
    __tablename__ = 'Contact'
    ContactID = Column(Integer, primary_key=True)
    Name = Column(String, unique=True)

    def __init__(self, name):
        self.Name = name

    def __repr__(self):
        return "<Contact ({})>".format(self.Name)


class Message(Base):
    __tablename__ = 'Message'
    MessageID = Column(Integer, primary_key=True)
    Text = Column(String)
    Created_Datetime = Column(DateTime, default=datetime.datetime.utcnow)
    ContactID = Column(Integer, ForeignKey('Contact.ContactID'))
    Contact = relationship('Contact', back_populates='Messages')

    def __init__(self, text, contact_id, creation_datetime=None):
        self.Text = text
        self.ContactID = contact_id
        if creation_datetime:
            self.Created_Datetime = creation_datetime

    def __repr__(self):
        return '<Message ({}, {})>'.format(self.Text, self.ContactID)


Contact.Messages = relationship('Message',
                                order_by=Message.Created_Datetime,
                                back_populates='Contact')

Base.metadata.create_all(engine)
