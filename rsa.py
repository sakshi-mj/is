import random
def gen_keys():
    p = 17
    q = 23
    n = p * q
    phi_n = (p-1)*(q-1)

    e = random.randrange(2,phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randrange(2,phi_n)

    d = modInverse(e, phi_n)
    return (e,n),(d,n)

def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

def encrypt(text, public_key):
    e,n = public_key
    return [pow(ord(char),e,n) for char in text]

def modInverse(e,phi_n):
    for d in range(2,phi_n):
        if (e*d)%phi_n == 1:
            return d
    return -1
def decrypt(cipher, pvt_key):
    d,n = pvt_key
    return ''.join(chr(pow(char, d, n)) for char in cipher)

public_key, pvt_key = gen_keys()
text = input("message: ")
cipher = encrypt(text, public_key)

print('pk: ', public_key)
print('prk: ', pvt_key)
print('encr: ', cipher)
print('decr: ', decrypt(cipher, pvt_key))
