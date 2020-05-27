from random import randrange, getrandbits

def is_prime(n, k=128):
    """ Test if a number is prime

        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do

        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generate_prime_candidate(length):
    """ Generate an odd integer randomly

        Args:
            length -- int -- the length of the number to generate, in bits

        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    print("[] Generating a prime number...")
    count = 0
    """ Generate a prime

        Args:
            length -- int -- length of the prime to generate, in bits

        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
        count += 1

    print "[] Finish generation... Takes", count, "tries.";
    return p

#print(generate_prime_number())

'''
       ========== GENERATED NUMBER ==========
       C3 3F 30 7F D2 B5 9B 66 AB D3 AB 54 CB
       31 C3 C4 7F 6A 85 CC 48 72 F5 51 E0 68
       06 12 BD BA 68 7E 72 68 53 40 C9 60 12
       4E 0D 16 D5 49 FD 00 17 AB 57 BD 8C A1
       3A 33 A6 63 76 7B 7A C7 78 D4 88 D0 A5
       6C 95 BC 43 8C 9C 93 1E 76 62 DC D7 27
       6D 13 FD 92 E6 7E 2F E1 62 28 C6 CB 06
       60 81 47 51 49 22 B9 D0 1E 2A 3D 76 0B
       8F 30 51 B2 88 E9 04 B5 2E D8 79 C0 23
       0C DC 8B 2B AF 8D 71 BA 5E 05 B1
'''
def printHex(num):
    str = ""
    count = 0
    while num > 0:
        if num % 16 < 10:
            str = chr(48 + (num % 16)     ) + str
        else:
            str = chr(65 + (num % 16) - 10) + str
        num //= 16

    print "\t\b========== GENERATED NUMBER ==========",
    for i in range(len(str)):
        if count % 26 == 0:
            print "\n\t",
        elif count % 2 == 0:
            print "",
        print "\b" + str[i],
        count += 1

p = generate_prime_number()
printHex(p)
print(p)
