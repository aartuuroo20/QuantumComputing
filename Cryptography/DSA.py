from random import randint
#parameter generation: select the primes q, p and generator g:
q = 11
p = 23
g = 4

print(f"q={p}, p={p}, g={g}")

#Alice chooses an integer randomly from {2..q-1}
alice_private_key = randint(2, q-1)  
print(f"Alice's private key is {alice_private_key}")

alice_public_key = (g ** alice_private_key) % p
print(f"Alice's public key is {alice_public_key}")

hash_dict={}
def mock_hash_func(inp):
    if not inp in hash_dict:
        hash_dict[inp] = randint(1,q)
    return hash_dict[inp]

alice_message = "Inspection tomorrow!"
alice_hash = mock_hash_func(alice_message)  # In reality, you'd use a hash function
print(f"Alice's message hash is: {alice_hash}")

def modular_inverse(k, q):
    for i in range(1, q):
        if (k * i) % q == 1:
            return i
    print('error! no inverse found!')
    return 0 

k = randint(1, q-1)  # Should be different for every message
r = (g ** k) % p % q
s = (modular_inverse(k, q) * (alice_hash + alice_private_key * r)) % q  
signature = (r, s)
print(f"Alice's signature is : {(r,s)}")

# Bob re-generates message hash using Alice's broadcast message
bob_hash = mock_hash_func(alice_message) 

#Bob computes auxiliary quantities w, u1, u2 and v
w = (modular_inverse(s,q)) % q  
u1 = (bob_hash * w) % q
u2 = (r * w) % q
v = ((g**u1 * alice_public_key**u2) % p) % q

if v == r:
    print("Signature is valid!")
else:
    print("Signature is invalid!")