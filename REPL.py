import RSA

str_features = [
    'Features:',
    'Generate public and private key',
    'Load keys',
    'Load message',
    'Encrypt message',
    'Decrypt message',
]

public_key = None
private_key = None
isKeysLoaded = False

isMsgLoaded = False

info = ''

position = 'dashboard'

while True:
    print('--- RSA Encryption ---')
    print('Status:')
    if info:
        print(f'info: {info}')
    print('[y] Keys loaded' if isKeysLoaded else '[X] Keys not loaded! load keys or generate key pair')
    if isKeysLoaded:
        print('[y] Message loaded')
    print('')

    if position == 'dashboard':
        [print(f'{i}.', val) for i, val in enumerate(str_features)]
        print('0. Exit')

    if position == 'load_keys':
        public_key, private_key = RSA.load_keys()

        isKeysLoaded = True
        position = 'dashboard'

    if position == 'load_message':
        message: str | None = None

        with open('message.txt', 'rb') as file:
            message = file.read().decode('ascii')
            file.close()

        isKeysLoaded = True
        position = 'dashboard'

    if position == 'encrypt_message':
        encrypted: str | None = None

        with open('message.bin', 'wb') as file:
            encrypted = RSA.encrypt(message, public_key=public_key)
            file.close()

        position = 'dashboard'

    if position == 'decrypt_message':
        decrypted: bytes | None = None

        with open('message.bin', 'rb') as file:
            decrypted = RSA.decrypt(message, public_key=public_key)
            file.close()

        position = 'dashboard'

    user_input = int(input('Input: '))

    if user_input == 0:
        break
    if user_input == 1:
        'generate_keys'

        public_key, private_key = RSA.generate_key_pair()
        RSA.save_key_pair(public_key=public_key, private_key=private_key)

        isKeysLoaded = True
    if user_input == 2:
        position = 'load_keys'
    if user_input == 3:
        position = 'load_message'
    if user_input == 4:
        position = 'encrypt_message'
    if user_input == 5:
        position = 'decrypt_message'

print('Features:')
print('2. Back')

print('2. Load keys')
print('- Filename (example: public_key.pem): ')
print('File not found!')
print('File loaded!')
print('1. Back')

print('3. Load message')
print('- Filename (example: message.txt): ')
print('Filename loaded!')
print('1. Back')

print('4. Encrypt message')
print('1. Load Public Key')
print('2. Load text file')
print('1. Insert message')
print('- Message: ')

print('5. Decrypt message')
print('[X] Keys not loaded!')
print('[X] Public key loaded!')
print('[X] Private key loaded!')

print('1. Load public key')
print('2. Load private key')
print('1. Load message')
print('2. Write message')
print('[!] Encrypted!')
print('[!] Encryption fails')
print('[?] Public key or private key might be invalid')
