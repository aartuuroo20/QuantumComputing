from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from os import urandom

# Bob's RSA key pair
private_key_Bob = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key_Bob = private_key_Bob.public_key()

print("Bob's private and public keys created")

Alice_long_secret = urandom(160)  # A 160 byte or 1280 bit random message
print("Alice's secret created")

Alice_encrypted_secret = public_key_Bob.encrypt(
    Alice_long_secret,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Alice's secret encrypted")

Bob_decrypted_secret = private_key_Bob.decrypt(
    Alice_encrypted_secret,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

assert Alice_long_secret == Bob_decrypted_secret, "Secrets do not match!"

# if we get here they match
print("Secrets match")

def key_derivation_function(secret, salt):
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,  # Desired key length
        salt=salt,
        info=None,
        backend=None
    )
    return hkdf.derive(secret)

common_salt = urandom(16)  # Random salt accessible to both Alice and Bob

symmetric_key_Alice = key_derivation_function(Alice_long_secret, common_salt)
symmetric_key_Bob = key_derivation_function(Bob_decrypted_secret, common_salt)

assert symmetric_key_Alice == symmetric_key_Bob, "Derived keys do not match!"
print(f"A symmetric key of length {len(symmetric_key_Alice)*8} bits was successfully derived by both Alce and Bob!")