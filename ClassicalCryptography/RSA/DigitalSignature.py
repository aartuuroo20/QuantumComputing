from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed

# Generate keys for Bob
bob_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
bob_public_key = bob_private_key.public_key()

# Generate keys for Alice
alice_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
alice_public_key = alice_private_key.public_key()

print("Private and Public keys generated for Bob and Alice.")

# Alice encrypts the message using Bob's public key
ciphertext = bob_public_key.encrypt(
    symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("ciphertext of symmetric key: ",ciphertext)

# Alice signs the ciphertext using her private key
digest = hashes.Hash(hashes.SHA256())
digest.update(ciphertext)
hash_to_sign = digest.finalize()

signature = alice_private_key.sign(
    hash_to_sign,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    Prehashed(hashes.SHA256())
)

print("signature: ",signature)

# Bob receives the ciphertext and signature
received_ciphertext = ciphertext
received_signature = signature

# Send signature and ciphertext here
print("Sending ciphertext and signature.....")

#Bob creates a hash of the ciphertext using the same algorithm used by Alice
digest = hashes.Hash(hashes.SHA256())
digest.update(received_ciphertext)
hash_to_verify = digest.finalize()

print("hash to verify: ",hash_to_verify)