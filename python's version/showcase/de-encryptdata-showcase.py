from rsa import getEncrypt, getDecrypt
from random import getrandbits
from millerrabin import generate_prime_number

# Generate private key & public key & randomize data
BITS = 1024
data = getrandbits(BITS)
p = generate_prime_number(BITS)
while True:
    q = generate_prime_number(BITS)
    if p != q:
        break
N = p*q
O = (p - 1)*(q - 1)
e = getEncrypt(O, N, p, q) # This number is used to encrypt the data
d = getDecrypt(e, O)       # This number is used to decrypt the data

# data = 2
# p = 2
# q = 7
# N = 14
# O = 6
# e = 5
# d = getD(e, O)

# Print out result
print "data: ", data
print "p: ", p
print "q: ", q
print "N: ", N
print "O: ", O
print "e: ", e
print "d: ", d

encrypted = pow(data, e, N)
decrypted = pow(encrypted, d, N)
print "data after encrypted: ", encrypted
print "data after decrypted: ", decrypted
