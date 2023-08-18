import RSA

# Encrypt and decrypt message using RSA

public_key = None
private_key = None

print('--- RSA Encryption ---')

print('Loading keys...')
is_keys_exists = RSA.check_keys_file()

if is_keys_exists:
    public_key, private_key = RSA.load_keys()
else:
    print('Keys not found! generating...')
    public_key, private_key = RSA.generate_key_pair()
    RSA.save_key_pair(public_key, private_key)


print(f"\n{private_key.save_pkcs1().decode('ascii')}")
print(f"{public_key.save_pkcs1().decode('ascii')}")

message = "RSA Encryption/Decryption"
print(f'Message: {message}')

encrypted = RSA.encrypt(message, public_key)
hex = RSA.bytes_to_hex(encrypted)
print(f'\nencrypted: {hex}')

decrypted = RSA.decrypt(encrypted, private_key)
print(f'\ndecrypted: {decrypted}')
