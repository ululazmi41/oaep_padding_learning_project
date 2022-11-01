import RSA
import os

str_features = [
    'Generate key pair',
    'Load keys',
    'write message',
    'Load message',
    'Encrypt message',
    'Decrypt message',
]

public_key = None
private_key = None
isKeysLoaded = False

encrypted: bytes = None
decrypted: str = None

message: str = ''
isMsgLoaded = False

info = ''

position = 'dashboard'

while True:
    os.system('cls')

    print('--- RSA Encryption ---')

    if info:
        print(f'info: {info}')
        info = ''

    print('[i] Private key loaded' if isKeysLoaded else '[X] Private key not loaded')
    print('[i] Public key loaded' if isKeysLoaded else '[X] Public key not loaded')
    print(
        f'[i] Message: {message[:20]}{"..." if len(message) > 20 else ""}' if isMsgLoaded else '[X] Message not loaded')
    print('')

    print('Features:')
    [print(f'{i+1}.', val) for i, val in enumerate(str_features)]
    print('0. Exit')

    user_input = int(input('Input: '))

    if user_input == 0:
        break

    if user_input == 1:
        'generate_keys'

        public_key, private_key = RSA.generate_key_pair()
        RSA.save_key_pair(public_key=public_key, private_key=private_key)

        isKeysLoaded = True

    if user_input == 2:
        'load_keys'

        public_key, private_key = RSA.load_keys()

        isKeysLoaded = True

    if user_input == 3:
        'write_message'

        message = input('message: ')

        isMsgLoaded = True

    if user_input == 4:
        'load_message'

        message = None

        with open('message.txt', 'rb') as file:
            message = file.read().decode('ascii')
            file.close()

        isKeysLoaded = True
        position = 'dashboard'

    if user_input == 5:
        'encrypt_message'

        if message:
            encrypted = RSA.encrypt(message=message, public_key=public_key)

        with open('message.bin', 'wb') as file:
            file.write(encrypted)

        info = 'Message encrypted! Saved in message.bin'

    if user_input == 6:
        'decrypt_message'

        if encrypted:
            decrypted = RSA.decrypt(
                encrypted=encrypted, private_key=private_key)

        with open('decrypted.txt', 'w') as file:
            file.write(decrypted)
            info = 'Decryption successful! saved in decrypted.txt'

exit(1)
print('2. Load key')
print('- Filename (example: public_key.pem, private_key.pem): ')
print('Error: file not found!')

print('3. Load message')
print('- Filename (example: message.txt): ')
print('Error: file not found!')

print('5. Decrypt message')
print('5. Load private key')
print('[X] Keys not loaded!')
print('[X] Public key loaded!')
print('[X] Private key loaded!')

print('[!] Decryption fails')
print('[?] Public key or private key might be invalid')
