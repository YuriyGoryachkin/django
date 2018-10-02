from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .SQL_Class_server import Client, Client_History, Contact_List, Base


class ServerStorage:
    """
    Класс для работы с базой клиентов
    """
    def __init__(self):
        engine = create_engine('sqlite:///DB/Server.sqlite')
        Session = sessionmaker(bind=engine)
        session = Session()
        self.session = session

    def __commit(self):
        self.session.commit()

    def verification(self, username, password, ip):
        verify = Client(username, password)
        result = self.session.query(Client).filter((Client.Name == username),
                                                   (Client.Password == password))
        if result.count() > 0:
            self.add_history(username, ip)
        else:
            self.session.add(verify)
            self.__commit()
            self.add_history(username, ip)

    def _get_client_by_username(self, username):
        """ Возвращает клиента с username """
        client = self.session.query(Client).filter(Client.Name == username).first()
        return client

    def add_history(self, username, ip):
        """ Добавление клиента и историю """
        client = self._get_client_by_username(username)
        if client:
            history = Client_History(client_id=client.ClientID, ip=ip)
            self.session.add(history)
            self.__commit()
        else:
            pass
