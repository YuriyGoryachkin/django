"""
Создание базы клиентов
"""
import datetime
import sys
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Numeric, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///DB/Server.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Client(Base):
    __tablename__ = 'Client'
    ClientID = Column(Integer, primary_key=True)
    Name = Column(String, unique=True)
    Password = Column(String, nullable=False)

    def __init__(self, name, password):
        self.Name = name
        self.Password = password

    def __repr__(self):
        return "<Client: {}\nPassword: {}\n>".format(self.Name, self.Password)


class Client_History(Base):
    __tablename__ = 'Client_History'
    Client_History_ID = Column(Integer, primary_key=True)
    ClientID = Column(Integer, ForeignKey('Client.ClientID'))
    Client = relationship('Client', back_populates='ClientHistories')
    Entry_Time = Column(DateTime, default=datetime.datetime.utcnow)
    IP_Host = Column(String)

    def __init__(self, client_id, ip, entry_time=None):
        self.IP_Host = ip
        self.ClientID = client_id
        if entry_time:
            self.Entry_Time = entry_time

    def __repr__(self):
        return "<Client_History ({}, {})>".format(self.IP_Host, self.ClientID)


class Contact_List(Base):
    __tablename__ = 'Contact_List'
    Contact_List_ID = Column(Integer, primary_key=True)
    ClientID = Column(Integer, ForeignKey('Client.ClientID'))
    ContactID = Column(Integer, ForeignKey('Client.ClientID'))

    def __init__(self, client_id, contact_id):
        self.ContactId = contact_id
        self.ClientId = client_id


Client.ClientHistories = relationship('Client_History',
                                      order_by=Client_History.Entry_Time,
                                      back_populates='Client')

Base.metadata.create_all(engine)
