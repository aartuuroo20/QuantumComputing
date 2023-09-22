from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

# Generate a private key for use in the signature
private_key = ec.generate_private_key(ec.SECP384R1())

message = b"A message to be signed"

# Sign the message
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Anyone can verify the signature with the public key
public_key = private_key.public_key()
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("The signature is valid.")
except:
    print("The signature is invalid.")