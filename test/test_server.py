# from src.socket_server import Server
import socket
import time
import json
import pytest
import pytest_socket

from server import Server


class SocketMock:
    def accept(self):
        print('accept')
        return SocketMock(), '127.0.0.1'

    def send(self, msg):
        print('send')
        return msg

    def close(self):
        print('close')

    def recv(self, data):
        print('recv: {}'.format(data))
        return data


def make_mock_socket():
    return SocketMock()


@pytest.fixture
def socket_fixture():
    return make_mock_socket()


def test_encode():
    assert b'byte-string' == 'byte-string'.encode('utf-8')


def test_explicitly_enable_socket(socket_enabled):
    assert socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def test_receive_response(socket_fixture):
    server = Server('127.0.0.1', 7777)
    server.make_tcp_socket(0)
    client_socket, client_address = socket_fixture.accept()
    msg = {
        'action': 'presence',
        'time': '',
        'type': 'status',
        'user': {
            'account_name': 'Test',
            'status': 'online'
        },
        'message': 'Test'
    }
    client_msg = json.dumps(msg, ensure_ascii=False)
    send_msg = client_msg.encode('utf-8')
    print('send: {}'.format(send_msg))
    # server.responses(client=client_socket, data=send_msg, w_clients=client_socket)
    print('answer_s: {}'.format(server.responses(client=client_socket, data=send_msg, w_clients=client_socket)))
    data = client_socket.recv(answer_s)
    print('recv: {}'.format(data))
    ret_test = {
        'response': 200,
        'time': '',
        'alert': 'OK',
    }
    assert json.loads(data.decode('utf-8')) == ret_test
