from collections import namedtuple
from random import choice, randrange
from string import ascii_letters

import numpy.polynomial as poly
from Crypto.Util.number import getPrime, inverse

Particapant = namedtuple('Particapant', ('id', 'key', 'power', 'prime'))


def random_str(length):
    return ''.join(choice(ascii_letters) for _ in range(length))


def generate_polynomial(count, secret):
    prime = getPrime(secret.bit_length() + 1)
    polynomial = [secret]
    for _ in range(count // 2):
        polynomial.append(randrange(1, prime))
    return prime, polynomial


def get_different_particapants(ps, length):
    ids = set()
    res = []
    choices = range(len(ps))
    while len(ids) != length and len(ids) != len(ps):
        p = ps[choice(choices)]
        if p.id in ids:
            continue
        res.append(p)
        ids.add(p.id)
    return res


def get_particapants(polynomial, count, prime):
    particapants = []
    values = set()
    max_j = 0
    max_power = count // 2
    for _ in range(count):
        j = max_j + 1
        while True:
            res = 0
            for power in range(max_power + 1):
                res += pow(j, power, prime) * polynomial[power]
            res %= prime
            if res in values:
                j += 1
                continue
            max_j = j
            particapants.append(Particapant(j, res, max_power, prime))
            values.add(res)
            break
    return particapants


def decode_secret(particapants):
    ls = []
    for p1 in particapants:
        coeff = 1
        res = poly.polynomial.Polynomial((1,))
        for p2 in particapants:
            if p1.id == p2.id:
                continue
            coeff *= p1.id - p2.id
            res = poly.polynomial.polymul(res, poly.polynomial.Polynomial((1, -p2.id)))[0]
        coeff = inverse(coeff, p1.prime)
        res = list((int(e) * coeff * p1.key) % p1.prime for e in res)
        ls.append(res)
    return sum(e[-1] for e in ls) % particapants[0].prime


def main():
    count = int(input("Enter participants count for protocol: "))
    if not count:
        count = 6
    secret = input("Enter secret text: ")
    if count < 2:
        print('Too few people!')
        exit(1)
    if not secret:
        secret = random_str(20).encode('ascii')

    print('Original secret:')
    print(' ', secret, end='\n\n')

    prime, polynomial = generate_polynomial(count, secret)
    del secret
    particapants = get_particapants(polynomial, count, prime)

    del prime, polynomial

    print('Check how many people can decrypt')
    for i in range(2, count + 1):
        ps = get_different_particapants(particapants, i)
        decoded_secret = decode_secret(ps)
        decoded_secret = decoded_secret.to_bytes((decoded_secret.bit_length() + 7) // 8, 'big')
        print(i)
        print(' ', decoded_secret, end='\n\n')


if __name__ == '__main__':
    main()
