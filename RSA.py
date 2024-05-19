"""RSA Algoritm."""

import binascii
import os
import rsa
from pathlib import Path

key_dir = 'Keys'


def generate_key_pair(bits: int = 2048) -> tuple[rsa.PublicKey, rsa.PrivateKey]:
    public_key, private_key = rsa.newkeys(bits)
    return public_key, private_key


def encrypt(message: str, public_key: rsa.PublicKey) -> bytes:
    encrypted = rsa.encrypt(message.encode('utf-8'), public_key)
    return encrypted


def decrypt(encrypted: bytes, private_key: rsa.PrivateKey) -> str:
    decrypted = rsa.decrypt(encrypted, private_key).decode('ascii')
    return decrypted


def save_signature(signature: bytes, filename: str = '') -> bool:
    signature_filename: str = 'signature'
    if filename != '':
        signature_filename = f'{filename}_{signature_filename}'
    with open(f'{signature_filename}.pem', 'wb') as file:
        file.write(signature)
        file.close()

    return True


def save_key_pair(public_key: rsa.PublicKey, private_key: rsa.PrivateKey, filename: str = '') -> bool:
    public_key_str = 'publicKey'
    private_key_str = 'privateKey'
    if filename != '':
        public_key_str = f'{filename}_{public_key_str}'
        private_key_str = f'{filename}_{private_key_str}'
    public_key_file = Path(f'{key_dir}\{public_key_str}.pem')
    private_key_file = Path(f'{key_dir}\{private_key_str}.pem')
    with public_key_file.open('wb') as file:
        file.write(public_key.save_pkcs1())
    with private_key_file.open('wb') as file:
        file.write(private_key.save_pkcs1())
    return True


def load_signature(filename: str = '') -> bytes:

    signature: bytes = None
    signature_filename: str = 'signature'

    if filename != '':
        signature_filename = f'{filename}_{signature_filename}'

    with open(f'{signature_filename}.pem', 'rb') as file:
        signature = file.read()

    return signature


def load_keys(filename: str = '') -> tuple[rsa.PublicKey, rsa.PrivateKey]:

    public_key_str: str = 'publicKey'
    private_key_str: str = 'privateKey'

    if filename != '':
        public_key_str = f'{filename}_{public_key_str}'
        private_key_str = f'{filename}_{private_key_str}'

    with open(f'{key_dir}\{public_key_str}.pem', 'rb') as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())

    with open(f'{key_dir}\{private_key_str}.pem', 'rb') as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read())

    return public_key, private_key


def check_keys_file(filename: str = '') -> bool:

    public_key_str: str = 'publicKey'
    private_key_str: str = 'privateKey'

    if filename != '':
        public_key_str = f'{filename}_{public_key_str}'
        private_key_str = f'{filename}_{private_key_str}'

    condition = os.path.isfile(f'{key_dir}\{public_key_str}.pem') and os.path.isfile(
        f'{key_dir}\{private_key_str}.pem')
    return condition


def check_signature_file(filename: str = '') -> bool:

    signature_filename: str = 'signature'

    if filename != '':
        signature_filename = f'{filename}_{signature_filename}'

    condition = os.path.isfile(f'{signature_filename}.pem')
    return condition


def signature_message(message: str, private_key, hash_method: str) -> bytes:
    signature = rsa.sign(message.encode('UTF-8'), private_key, hash_method)
    return signature


def verify_signature(message: str, signature: bytes, public_key: rsa.PublicKey) -> str:
    result = rsa.verify(message.encode('UTF-8'), signature, public_key)
    return result


def bytes_to_hex(text: bytes) -> str:
    result = binascii.hexlify(text).decode('ascii')
    return result
