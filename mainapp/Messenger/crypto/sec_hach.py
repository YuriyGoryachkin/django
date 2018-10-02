import hashlib
import binascii


def crypto_hash_psw(psw, key='sha256', cr_salt=b'c2h5oh'):
    """
    Шифрование пароля
    :param psw:
    :param key:
    :param cr_salt:
    :return:
    """
    secret_key = hashlib.pbkdf2_hmac(key, psw.encode('utf-8'), cr_salt, 100000)
    password = binascii.hexlify(secret_key)
    return password.decode('utf-8')
