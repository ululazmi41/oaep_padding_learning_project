import binascii
import os
import rsa

# https://stuvel.eu/python-rsa-doc/usage.html#encryption-and-decryption


def generator_key(bits: int = 2048):
    public_key, private_key = rsa.newkeys(bits)
    return public_key, private_key


def encrypt(message, public_key):
    encrypted = rsa.encrypt(message.encode('utf-8'), public_key)
    return encrypted


def decrypt(encrypted, private_key):
    decrypted = rsa.decrypt(encrypted, private_key)
    return decrypted


def save_key(key, filename):
    with open(f'{filename}', 'wb') as file:
        file.write(key.save_pkcs1())
        file.close()


if not os.path.isfile('public.pem') or not os.path.isfile('private.pem'):
    public_key, private_key = generator_key()
    save_key(public_key, 'public.pem')
    save_key(private_key, 'private.pem')

public_key = None
private_key = None

with open('public.pem', 'rb') as file:
    public_key = rsa.PublicKey.load_pkcs1(file.read())

with open('private.pem', 'rb') as file:
    private_key = rsa.PrivateKey.load_pkcs1(file.read())

print(f"Private key: {private_key.save_pkcs1().decode('ascii')}")
print(f"\nPublic key: {public_key.save_pkcs1().decode('ascii')}")

message = "Saya adalah mahasiswa yang jujur"
encrypted = encrypt(message, public_key)
hex = binascii.hexlify(encrypted)
print(f'\nencrypted: {hex}')

decrypted = decrypt(encrypted, private_key)
print(f'\ndecrypted: {decrypted}')
