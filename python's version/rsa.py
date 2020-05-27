from millerrabin import generate_prime_number
from random import randrange, getrandbits
from gcds import gcd, extended_gcd

def getEncrypt(O, N, p, q):
    """
        We need to find e that:
            e is coprime with N and O,
            or GCD(e, N) = 1 and GCD(e, O) = 1.
    """
    e = -1
    while True:
        e = randrange(2, O)
        if gcd(e, N) == 1 and gcd(e, O) == 1:
            break
    return e

def getDecrypt(e, O):
    """
        Find d such a way that:
            de = 1 (mod O)
        Or:
            de + Oy = 1

        Since 1 = GCD(O, e), we could achieve this by using
        Euclidean algorithm for extended GCD. In other word,
        we need to find e and y such that:
            de + Oy = GCD(O, e)
    """
    y, d, gcd = extended_gcd(O, e)
    if d < 0:
        d += O
    if d == e:
        d += O
    return d

def generate_keys(length=1024):
    """
        Generates 2 private and public keys, each contains
        a pair of numbers.
    """

    #Generates 2 primes by Miller-Rabin Algorithm
    p = generate_prime_number(length / 2)
    while True:
        q = generate_prime_number(length / 2)
        if p != q:
            break

    common_half   = p * q                                          # First number in pair, appears in both keys.
    O_common_half = (p - 1)*(q - 1)                                # Phi(half_key), for generating another halves of 2 keys.
    public_half   = getEncrypt(O_common_half, common_half, p, q)   # Use public half to encrypt data.
    private_half  = getDecrypt(public_half, O_common_half)         # Use private half to decrypt data.

    private_key = private_half, common_half, length
    public_key  = public_half , common_half, length

    return public_key, private_key
