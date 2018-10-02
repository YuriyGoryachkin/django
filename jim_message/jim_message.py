"""
Протокол JIM
"""
import json
import time
from binascii import hexlify

from crypto.sec_mes import Crypto_Message

time = time.ctime(time.time())


class JIMMessageClient:
    """
    Протокол для клиента
    """
    def __init__(self, user_name):
        self.user_name = user_name

    def presence_msg(self):
        """
        Presence-сообщение
        :return:
        """
        action = 'presence'
        type = 'status'
        status = 'online'
        message = ''
        return self.response_client(action, type, status, message)

    def authenticate_msg(self, password, msg='online'):
        """
        Аутентификация клиента или регистрация
        """
        action = 'authenticate'
        type = 'status'
        status_type = 'password'
        status = password
        message_type = 'status'
        message = msg
        return self.response_client(action, type, status, message,
                                    status_type=status_type, message_type=message_type)


    def msg_msg(self, msg):
        """
        Передача сообщений в чат
        """
        action = 'msg'
        type = 'write'  # Запись в чат
        status = 'online'
        message = msg
        return self.response_client(action, type, status, message)

    def receiver(self):
        action = 'msg'
        type = 'read'   # Чтение чата
        status = 'online'
        message = '[Hi]'
        return self.response_client(action, type, status, message)

    def join_msg(self):
        action = 'join'
        status = 'online'
        pass

    def leave_msg(self):
        action = 'leave'
        status = 'online'
        pass

    def quit_msg(self):
        action = 'quit'
        type = 'status'
        status = 'offline'
        message = '[Bye bye]'
        return self.response_client(action, type, status, message)

    def response_client(self, action, type, status, message, status_type='status', message_type='message'):
        """
        Формирование сообщений
        :param action:
        :param type:
        :param status:
        :param message:
        :param status_type:
        :param message_type:
        :return:
        """
        msg = {
            'action': action,
            'time': time,
            'type': type,
            'user': {
                'account_name': self.user_name,
                status_type: status
            },
            message_type: message
        }
        client_msg = json.dumps(msg, ensure_ascii=False)
        msg_crypto_client = Crypto_Message()
        msg_for_crypto = msg_crypto_client._encrypt(client_msg.encode())
        return msg_for_crypto
        # return client_msg.encode()


class JIMMessageServer:
    """
    Протокол для сервера
    """
    def __init__(self):
        pass

    def good_response(self):
        response = 200
        type_msg = 'alert'
        message = 'OK'
        return self.response_server(response, type_msg, message)

    def response_1xx(self, code, msg):
        type_msg = 'alert'
        message = msg
        return self.response_server(code, type_msg, message)

    def response_2xx(self, code):
        type_msg = 'alert'
        message = ''
        return self.response_server(code, type_msg, message)

    def response_4xx(self, code, msg=''):
        type_msg = 'error'
        message = msg
        return self.response_server(code, type_msg, message)

    def response_5xx(self, code):
        type_msg = 'error'
        message = 'Error server'
        return self.response_server(code, type_msg, message)

    def response_6xx(self, code, user, msg):
        response = code
        message = msg
        return self.response_ser_msg(response, user, message)

    def response_server(self, response, type_msg, message):
        """
        Формирование сообщений
        :param response:
        :param type_msg:
        :param message:
        :return:
        """
        msg = {
            'response': response,
            'time': time,
            type_msg: message,
        }
        server_msg = json.dumps(msg, ensure_ascii=False)
        msg_crypto_server = Crypto_Message()
        msg_for_crypto = msg_crypto_server._encrypt(server_msg.encode())
        return msg_for_crypto
        # return server_msg.encode()

    def message(self):
        response = 'msg'
        message = 'test'
        return self.response_ser_msg(response, message)

    def response_ser_msg(self, response, user, message):
        """
        Формирование сообщений для рассылки
        :param response:
        :param user:
        :param message:
        :return:
        """
        msg = {
            'response': response,
            'time': time,
            'user': user,
            'message': message
        }
        server_msg = json.dumps(msg, ensure_ascii=False)
        msg_crypto_server = Crypto_Message()
        msg_for_crypto = msg_crypto_server._encrypt(server_msg.encode())
        return msg_for_crypto
        # return server_msg.encode()
