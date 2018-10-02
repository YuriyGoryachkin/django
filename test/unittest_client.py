# Работа с unittest
import unittest
from socket import *

from client import *
from jim_message.jim_message import JIMMessageClient

class TestClient(unittest.TestCase):

    def setUp(self):
        # Начальные действия
        self.socket= socket(AF_INET, SOCK_STREAM)
        self.socket.bind(('127.0.0.2', 7777))
        self.socket.listen(1)
        self.client = Client('TEST')
        self.test_JIM = JIMMessageClient

    def tearDown(self):
        # Завершающие действия
        self.socket.close()

    def test_connect_server(self):
        self.assertEqual(self.client.connect_server('127.0.0.2', 7777), True, 'Ошибка Client.connect_server()')
        self.client.disconnect_server()

    def test_start_JIM(self):
        self.assertEqual(self.client.start_JIM(self.test_JIM), True, 'Ошибка start_JIM()')

if __name__ == "__main__":
    unittest.main()