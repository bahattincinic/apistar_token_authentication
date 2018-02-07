import hashlib
import binascii


def hash_password(password):
    salt = '0394a2ede332c9a13eb82e9b24631604c31df978b4e2f0fbd2c549944f9d79a5'
    dk = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt.encode(), 100000
    )
    return binascii.hexlify(dk)

