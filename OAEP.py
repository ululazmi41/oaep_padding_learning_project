import os
from functools import reduce
from hashlib import sha256
import numpy as np
import math


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
    hLen = hash_func().digest_size

    k = RSA_modulo
    PS = (0).to_bytes(k-mLen-2*hLen-2)

    DB = lHash + PS + (1).to_bytes(1) + message.encode('UTF-8')

    seed = os.urandom(hLen)
    dbMask = MGF1(seed=seed, length=k-hLen-1, hash_func=hash_func)

    maskedDB = xor_bytes(DB, dbMask)
    seedMask = MGF1(maskedDB, hLen)
    maskedSeed = xor_bytes(seed, seedMask)

    return b'\x00' + maskedSeed + maskedDB


RSA_modulo = 65537

padded = pad(message='Aneko Ikezawa',
             RSA_modulo=RSA_modulo, hash_func=sha256)
print(padded)

exit()

# print(int.from_bytes(a, 'big') ^ int.from_bytes(b, 'big'))


seed = os.urandom(256)
hash = sha256
hLen = hash.block_size

print(f'result: {MGF1(seed, hLen, hash).hex()}')

# Bytes -> Int -> Bytes

# a = os.urandom(16)
# print(int.from_bytes(a, 'big'))
# print((int.from_bytes(a, 'big')).to_bytes(len(a), byteorder='big'))
