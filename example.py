"""Example of using OAEP on RSA Algorithm."""

from hashlib import sha256
import RSA
import OAEP

message = 'RSA OAEP'
RSA_modulo = 65337

print('generating key pair...')
publicKey, privateKey = RSA.generate_key_pair()

print('signing message...')
signature = RSA.signature_message(message=message, private_key=privateKey, hash_method='SHA-256')

print('padding message...')
padded = OAEP.pad(message=message, RSA_modulo=RSA_modulo, hash_func=sha256)

print('unpadding message...')
unpadded = OAEP.unpad(padded=padded, RSA_modulo=RSA_modulo, hash_func=sha256)

print('validating signature...')
isSignatureValid = RSA.verify_signature(message=unpadded, signature=signature, public_key=publicKey)

if isSignatureValid:
    print(f'message: {unpadded}')
else:
    print('decrypt error: signature does not match')
