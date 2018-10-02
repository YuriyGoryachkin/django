from test import unittest_server, unittest_client
import unittest


def test_unit(module):
    unittest.main(module)


if __name__ == '__main__':
    test_unit(unittest_server)
