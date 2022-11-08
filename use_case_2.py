import RSA

# Signing message

print('--- RSA Encryption Signature ---')

message_1: str = 'Rekayasa Perangkat Lunak'
message_2 = 'Software Engineering'

print(f'message 1: {message_1}')
print(f'message 2: {message_2}')

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


signature = RSA.signature_message(
    message_1, alice_private_key, 'SHA-256')

signature_in_ascii = RSA.bytes_to_hex(signature)
print(f'\nmessage 1 signature: {signature_in_ascii}')

verify_message_1 = RSA.verify_signature(
    message_1, signature, alice_public_key)

print(f'\nverifying: message 1 with signature')
print(f'Result: {verify_message_1}')

print(f'\nverifying: message 2 with signature')
try:
    verify_message_2 = RSA.verify_signature(
        message_2, signature, alice_public_key)
    print(f'Result: {verify_message_2}')
except Exception as e:
    print(f'Result: {e}')
