from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Each party generates a private key
private_key1 = ec.generate_private_key(ec.SECP384R1())
private_key2 = ec.generate_private_key(ec.SECP384R1())

# They exchange public keys
public_key1 = private_key1.public_key()
public_key2 = private_key2.public_key()

# Each party uses their own private key and the other party's public key
# to derive the shared secret
shared_key1 = private_key1.exchange(ec.ECDH(), public_key2)
shared_key2 = private_key2.exchange(ec.ECDH(), public_key1)

# The shared secrets are the same
assert shared_key1 == shared_key2
print("Keys checked to be the same")