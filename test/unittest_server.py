# # Работа с unittest
# import unittest
# from socket import *
#
# # from server import *
# from server import *
# from jim_message.jim_message import JIMMessageServer
#
#
#
# class TestServer(unittest.TestCase):
#
#     def setUp(self):
#         # Начальные действия
#         self.server = Server('127.0.0.1', 7777)
#         self.test_JIM = JIMMessageServer
#
#     def tearDown(self):
#         # Завершающие действия
#         pass
#
#     def test_make_tcp_socket(self):
#         self.assertEqual(self.server.make_tcp_socket(), True, "Ошибка Server.make_tcp_socket()")
#         self.server.sock.close()
#
#     def test_start_JIM(self):
#         self.assertEqual(self.server.start_JIM(self.test_JIM), (True, 'JIM protocol: OK'),
#                          'Ошибка start_JIM()')
#
#
# # if __name__ == '__main__':
# #     unittest.main()
