import RSA
str_features = [
    'Features:',
    'Generate public and private key',
    'Load keys',
    'Load message',
    'Encrypt message',
]

isKeysLoaded = False
position = 'dashboard'

while True:
    print('--- RSA Encryption ---')
    print('Status:')
    print('[y] Keys loaded' if isKeysLoaded else '[X] Keys not loaded! load keys or generate key pair')
    print('')

    if position == 'dashboard':
        [print(f'{i}.', val) for i, val in enumerate(str_features)]
    if position == 'generate_key':
        print('1. Save keys')

    print('0. Exit')

    user_input = int(input('Input: '))
    if user_input == 0:
        break
    if user_input == 1:
      position = 'generate_keys'

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
