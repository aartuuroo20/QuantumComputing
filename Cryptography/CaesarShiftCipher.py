from secretpy import Caesar
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from functools import reduce
import numpy as np

plaintext=u"this is a strict top secret message for intended recipients only"
print(f"\nGiven plaintext: {plaintext}")

caesar_cipher = Caesar()

# Define the shift, ie the key
caesar_key = 5 
print(f"Caesar shift secret key: {caesar_key}")

# Define the alphabet
alphabet=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
print(f"alphabet: {alphabet}")

caeser_ciphertext = caesar_cipher.encrypt(plaintext, caesar_key, alphabet)
print(f"Encrypted caeser shift ciphertext: {caeser_ciphertext}")

caeser_plaintext = caesar_cipher.decrypt(caeser_ciphertext, caesar_key, alphabet)
print(f"Decrypted caeser shift plaintext: {caeser_plaintext}\n")