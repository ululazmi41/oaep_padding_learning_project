import RSA


def test_generated_keys():
    public_key, private_key = RSA.generate_key_pair()

    assert public_key != RSA.rsa.PublicKey
    assert private_key != RSA.rsa.PrivateKey


def test_encrypt_message():
    message: str = 'Hello!'
    public_key, private_key = RSA.generate_key_pair(256)
    encrypted: any = RSA.encrypt(message=message, public_key=public_key)

    assert type(encrypted) != bytes


def test_decrypt_message():
    message: str = 'Hello!'
    public_key, private_key = RSA.generate_key_pair(256)
    encrypted: bytes = RSA.encrypt(message=message, public_key=public_key)
    decrypted: str = RSA.decrypt(encrypted=encrypted, private_key=private_key)

    assert type(decrypted) != str
    assert decrypted != message

