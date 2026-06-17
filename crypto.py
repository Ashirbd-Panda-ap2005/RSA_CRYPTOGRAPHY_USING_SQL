import random

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def gcd(a, b):
    """Finds the greatest common divisor."""
    while b:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    """Calculates the modular multiplicative inverse using Extended Euclidean Algorithm."""
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi % e
        temp_phi = e
        e = temp2
        
        x = x2 - temp1 * x1
        y = y2 - temp1 * y1
        
        x2, x1 = x1, x
        y2, y1 = y1, y
        
    if temp_phi == 1:
        return y2 + phi if y2 < 0 else y2
    return None

def generate_rsa_keys():
    """Generates an actual RSA Public and Private key pair."""
    # Pick two distinct prime numbers
    primes = [i for i in range(100, 300) if is_prime(i)]
    p = random.choice(primes)
    q = random.choice([x for x in primes if x != p])
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose public exponent e coprime to phi
    e = 3
    while gcd(e, phi) != 1:
        e += 2
        
    # Calculate private exponent d
    d = multiplicative_inverse(e, phi)
    
    return (e, n), (d, n)  # Returns (Public Key Pair, Private Key Pair)

def encrypt(plaintext, public_key):
    """Encrypts text using public key: C = (M^e) mod n"""
    e, n = public_key
    # Convert characters to characters' ASCII numbers, compute power, and join with commas
    cipher_list = [str(pow(ord(char), e, n)) for char in plaintext]
    return ",".join(cipher_list)

def decrypt(ciphertext_str, private_key):
    """Decrypts text using private key: M = (C^d) mod n"""
    d, n = private_key
    # Split the comma-separated string back to big integers, compute math, and join as text
    cipher_integers = [int(x) for x in ciphertext_str.split(",")]
    decrypted_chars = [chr(pow(num, d, n)) for num in cipher_integers]
    return "".join(decrypted_chars)
