from secretpy import Caesar
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from functools import reduce
import numpy as np

plaintext=u"this is a strict top secret message for intended recipients only"
print(f"\nGiven plaintext: {plaintext}")

# Define the alphabet
alphabet=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
print(f"alphabet: {alphabet}")

# lamba defines an inline function in this case that takes two values a,b with the resulting expression of a+b
# reduce uses a two-argument function(above), and applies this to all the entries in the list (random alphabet characters) cumulatively
aes_key = reduce(lambda a, b: a + b, [np.random.choice(alphabet) for i in range(16)])

print(f'AES secret key: {aes_key}')

aes_initialization_vector = reduce(lambda a, b: a + b, [np.random.choice(alphabet) for i in range(16)])
print(f"AES initialization vector: {aes_initialization_vector}")

# The encryptor is setup using the key & CBC. In both cases we need to convert the string (utf-8) into bytes
sender_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(aes_initialization_vector, 'utf-8')))
aes_encryptor = sender_aes_cipher.encryptor()

# update can add text to encypt in chunks, and then finalize is needed to complete the encryption process
aes_ciphertext = aes_encryptor.update(bytes(plaintext, 'utf-8')) + aes_encryptor.finalize()

# Note the output is a string of bytes
print(f"Encrypted AES ciphertext: {aes_ciphertext}")

# Similar setup of AES to what we did for encryption, but this time, for decryption
receiver_aes_cipher = Cipher(algorithms.AES(bytes(aes_key, 'utf-8')), modes.CBC(bytes(aes_initialization_vector, 'utf-8')))
aes_decryptor = receiver_aes_cipher.decryptor()

# Do the decryption
aes_plaintext_bytes = aes_decryptor.update(aes_ciphertext) + aes_decryptor.finalize()

# convert back to a character string (we assume utf-8)
aes_plaintext = aes_plaintext_bytes.decode('utf-8')

print(f"Decrypted AES plaintext: {aes_plaintext}")