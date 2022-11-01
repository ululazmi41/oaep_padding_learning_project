import RSA

print('--- RSA Encryption with Signature ---')

message_1: str = 'Rekayasa Perangkat Lunak'
message_2 = 'Software Engineering'
message_3 = 'Teknik Informatika'
message_4 = 'Politeknik Negeri Bengkalis'

print(f'\nmessage 1: {message_1} <- (Alice)')
print(f'message 2: {message_2}')
print(f'message 3: {message_3}')
print(f'message 4: {message_4}')

print('\n---- Message Signature ----')

print('\nLoading Alice\'s keys...')
is_alice_keys_exists = RSA.check_keys_file('Alice')

alice_public_key = None
alice_private_key = None

if is_alice_keys_exists:
    alice_public_key, alice_private_key = RSA.load_keys(filename='Alice')
else:
    print('Keys not found! generating keys for Alice...')
    alice_public_key, alice_private_key = RSA.generate_key_pair()
    RSA.save_key_pair(public_key=alice_public_key,
                      private_key=alice_private_key, filename='Alice')

signature: bytes | None = None

isSignatureExists = RSA.check_signature_file()

print('Checking signature...')
if isSignatureExists:
    signature = RSA.load_signature()
else:
    print('Signature not found! generating...')
    signature = RSA.signature_message(
        message_1, alice_private_key, 'SHA-256')

    RSA.save_signature(signature)

print('\n---- Message Encryption ----')

is_keys_exists = RSA.check_keys_file()

public_keys = None
private_keys = None

print('Loading public key...')
if is_keys_exists:
    public_key, private_key = RSA.load_keys()
else:
    print('Keys not found! generating keys...')
    public_key, private_key = RSA.generate_key_pair()
    RSA.save_key_pair(public_key=public_key,
                      private_key=private_key)

encrypted = RSA.encrypt(message=message_1, public_key=public_key)
encrypted_in_hex = RSA.bytes_to_hex(encrypted)
print(f'\nencrypted: {encrypted_in_hex}')

print('\n---- Message Decryption ----')

public_keys = None
private_keys = None
is_keys_exists = RSA.check_keys_file()

print('Loading public key...')
if is_keys_exists:
    public_key, private_key = RSA.load_keys()
else:
    print('Keys not found! generating keys...')
    public_key, private_key = RSA.generate_key_pair()
    RSA.save_key_pair(public_key=public_key,
                      private_key=private_key)

decrypted = RSA.decrypt(encrypted=encrypted, private_key=private_key)
print(f'\ndecrypted: {decrypted}')

print('\n---- Signature Verification ----')

signature: bytes = RSA.load_signature()
signature_in_hex = RSA.bytes_to_hex(signature)
message = decrypted
result = None

print(f'\nMessage: {message}')
print(f'Signature: {signature_in_hex}')

print('\nVerifying signature...')
try:
    result = RSA.verify_signature(message, signature, alice_public_key)
    print(f'Result: Message is verified, signature is hashed with {result}')
except Exception as e:
    print(f'Result: Error! {type(e)} -> {e}')
