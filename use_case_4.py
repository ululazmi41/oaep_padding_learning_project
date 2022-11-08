import RSA
import OAEP
from hashlib import sha256

# RSA + OAEP (just combining, not using both method called RSA-OAEP)
# Flow:
# Generate Key Pair -> Signature given message -> pad using OAEP -> unpad -> verify signature

message: str = 'Aneko Ikezawa'
print('Generating key pair...')
publicKey, privateKey = RSA.generate_key_pair()
RSA_modulo: int = 65337

print('Signing message...')
signature = RSA.signature_message(
    message=message, private_key=privateKey, hash_method='SHA-256')
print('Padding message...')
padded = OAEP.pad(message=message, RSA_modulo=RSA_modulo, hash_func=sha256)

print('Unpadding message...')
unpadded = OAEP.unpad(padded=padded, RSA_modulo=RSA_modulo, hash_func=sha256)
print('Checking message...')
isMessage = RSA.verify_signature(
    message=unpadded, signature=signature, public_key=publicKey)

if isMessage:
    print(f'Message: {unpadded}')
else:
    print(f'Signature not match')
