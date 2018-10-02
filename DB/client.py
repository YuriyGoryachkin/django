from .SQL_Class_client import Contact, Message
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ClientStorage:
    """
    Класс для работы с клиентской базой
    """
    def __init__(self, name):
        """
        Инициализация клиентской базы
        :param name:
        """
        self.name = name
        engine = create_engine('sqlite:///DB/Client.sqlite')
        Session = sessionmaker(bind=engine)
        session = Session()
        self.session = session

    def __commit(self):
        self.session.commit()

    def add_contact(self, username):
        new_contact = Contact(username)
        result = self.session.query(Contact).filter(Contact.Name == username)
        if result.count() > 0:
            pass
        else:
            self.session.add(new_contact)
            self.__commit()

    def _get_contact_by_username(self, username):
        contact = self.session.query(Contact).filter(Contact.Name == username).first()
        return contact

    def add_message(self, username, text):
        """ Добавляем историю сообщений """
        # contact = self._get_contact_by_username(username)
        contact =self.session.query(Contact).filter(Contact.Name == username).first()
        if contact:
            new_message = Message(text=text, contact_id=contact.ContactID)
            self.session.add(new_message)
            self.__commit()
        else:
            self.__commit()
