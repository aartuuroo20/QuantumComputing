! pip install cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes

symmetric_key = Fernet.generate_key()
print(f"\nSymmetric key generated by Alice: {symmetric_key}")

# Bob generates a 2048-bit RSA key pair
bob_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
bob_public_key = bob_private_key.public_key()
print(f"Public key broadcast by Bob: {bob_public_key}")
print(f"\nPublic numbers in Bobs' public key: {bob_public_key.public_numbers()}")

# Encryption
ciphertext = bob_public_key.encrypt(
   symmetric_key,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)

print("Ciphertext:", ciphertext)

# Bob decrypts ciphertext to access the symmetric key
decrypted_symmetric_key = bob_private_key.decrypt(
   ciphertext,
   padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA256()),
       algorithm=hashes.SHA256(),
       label=None
   )
)

print("Decrypted key:", decrypted_symmetric_key)
assert decrypted_symmetric_key == symmetric_key