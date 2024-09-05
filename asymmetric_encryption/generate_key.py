import random
import math
from sympy import mod_inverse, isprime

def generate_large_prime(bits):
    """Generate a large prime number with the specified number of bits."""
    while True:
        num = random.getrandbits(bits)
        if isprime(num):  # Use isprime from sympy
            return num

def generate_rsa_keys(bits=512):
    """Generate RSA public and private keys."""
    # 1. Select two large prime numbers
    p = generate_large_prime(bits // 2)
    q = generate_large_prime(bits // 2)

    # 2. Compute the modulus n
    n = p * q

    # 3. Compute Euler's totient function φ(n)
    phi_n = (p - 1) * (q - 1)

    # 4. Choose the public exponent e
    e = 65537  # A commonly used public exponent

    # Ensure e and φ(n) are coprime
    if math.gcd(e, phi_n) != 1:
        raise ValueError("e must be coprime with φ(n)")

    # 5. Compute the private exponent d
    d = mod_inverse(e, phi_n)

    # Return the public and private keys
    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

# Generate keys
public_key, private_key = generate_rsa_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)
