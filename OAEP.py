import os
from functools import reduce
from hashlib import sha256
import numpy as np
import math


def find_PS_len(PS: bytes) -> int | bool:
    for i in range(len(PS)):
        if PS[i] == 1:
            ps_end = i
            return ps_end
    return False


def to_bytes(x: int): return (x).to_bytes(math.floor(math.log(x, 256))+1)


def MGF1(seed: bytes, length: int, hash_func=sha256) -> bytes:
    hLen: int = hash_func().block_size
    if length > (hLen << 32):
        raise ValueError('Mask too long')
    T: bytes = b''
    counter = 0
    while len(T) < length:
        c = (counter).to_bytes(4, 'big')
        T += hash_func(seed+c).digest()
        counter += 1
    return T[:length]


# Numpy
# https://stackoverflow.com/questions/29408173/byte-operations-xor-in-python
def xor_bytes(a: bytes, b: bytes) -> bytes:
    a_int = np.frombuffer(a, dtype=np.uint8)
    b_int = np.frombuffer(b, dtype=np.uint8)
    result = (a_int ^ b_int).tobytes()
    return result


# No-library
def xor_bytes_nl(a: bytes, b: bytes) -> bytes:
    xor_ab = [i ^ j for i, j in zip(a, b)]
    in_bytes = [(k).to_bytes(1, 'big')for k in xor_ab]
    # https://www.geeksforgeeks.org/reduce-in-python/
    concat = reduce(lambda a, b: a+b, in_bytes)
    return concat


def pad(message: str, RSA_modulo: int, hash_func=sha256) -> bytes:

    label: str = 'Aneko'
    lHash: bytes = hash_func(label.encode('UTF-8')).digest()

    mLen: int = len(message)
    hLen: int = hash_func().digest_size

    k: int = RSA_modulo
    PS: bytes = (0).to_bytes(k-mLen-2*hLen-2)

    DB: bytes = lHash + PS + (1).to_bytes(1) + message.encode('UTF-8')

    seed: bytes = os.urandom(hLen)
    dbMask: bytes = MGF1(seed=seed, length=k-hLen-1, hash_func=hash_func)

    maskedDB: bytes = xor_bytes(DB, dbMask)
    seedMask: bytes = MGF1(maskedDB, hLen)
    maskedSeed: bytes = xor_bytes(seed, seedMask)

    return b'\x00' + maskedSeed + maskedDB


def unpad(padded: bytes, RSA_modulo: int, hash_func=sha256) -> bytes:

    label: str = 'Aneko'
    lHash: bytes = hash_func(label.encode('UTF-8'))
    hLen: int = lHash.digest_size
    k: int = RSA_modulo

    zero_bytes: bytes = padded[:1]
    maskedSeed: bytes = padded[1:1+hLen]
    maskedDB: bytes = padded[1+hLen:]

    seedMask: bytes = MGF1(maskedDB, hLen)
    seed: bytes = xor_bytes(maskedSeed, seedMask)
    dbMask: bytes = MGF1(seed, k-hLen-1)
    DB: bytes = xor_bytes(maskedDB, dbMask)

    lHash: bytes = DB[:hLen]
    lPS: int = find_PS_len(DB[hLen:])
    PS: bytes = DB[hLen:lPS]
    one_byte: bytes = DB[hLen+lPS]
    message: bytes = DB[hLen+lPS+1:]

    return message.decode()


RSA_modulo = 65537

padded = pad(message='Aneko Ikezawa', RSA_modulo=RSA_modulo, hash_func=sha256)
unpadded = unpad(padded=padded, RSA_modulo=RSA_modulo)
print(unpadded)

# Pad message
# padded = pad(message='Aneko Ikezawa',
#              RSA_modulo=RSA_modulo, hash_func=sha256)

# Save padded message
# with open('padded.bin', 'wb') as file:
#     file.write(padded)

# Open padded message
# padded: bytes = None
#     file.close()# with open('padded.bin', 'rb') as file:
#     padded = file.read()
#     file.close()
# unpadded = unpad(padded, RSA_modulo, sha256)

# MGF1 Manual Testing
# seed = os.urandom(256)
# hash = sha256
# hLen = hash.block_size

# print(f'result: {MGF1(seed, hLen, hash).hex()}')

# Bytes -> Int -> Bytes
# a = os.urandom(16)
# in_integer = int.from_bytes(a)
# in_bytes = to_bytes(in_integer)
