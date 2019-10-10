import random


def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True


def gcd(a: int, b: int) -> int:
    while (a % b != 0):
        c = a % b
        a = b
        b = c
    return b 


def multiplicative_inverse(e: int, phi: int) -> int:
    div = []
    rows = 0
    phi_temp = phi
    while phi_temp % e != 0:
        div.append(phi_temp // e)
        phi_temp, e = e, phi_temp % e
        rows += 1
    x = 0
    y = 1
    for i in range(rows - 1, -1, -1):
        x, y = y, x - (y * div[i])
    return y % phi


def generate_keypair(p: int, q: int) -> ((int, int), (int, int)):

    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)
