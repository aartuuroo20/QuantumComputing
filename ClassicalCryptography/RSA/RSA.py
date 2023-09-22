# Function to compute the gcd (greatest common divisor) 
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
print("gcd(50,10) =",gcd(50,10))
print("gcd(99,1033) =",gcd(99,33))
print("gcd(59,9) =",gcd(59,9))

# Choosing two prime numbers and keep them secret
p = 13
q = 19
print("The secret prime numbers p and q are:", p, q)

n = p * q
print("modulus n (p*q)=",n)

# Compute Euler's totient function, φ(n) and keep it secret
phi = (p-1) * (q-1)
print("The secret Euler's function (totient) [phi(n)]:",phi)

e = 2
while (e < phi):
    if (gcd(e, phi)==1):
        break
    else:
        e += 1
print("Public Key (e):",e)

d = 1
while(True):
    if((d*e) % phi == 1):
        break
    else:
        d += 1
print("Private Key (d):",d)

public = (e, n)
private = (d, n)

print(f"The Public key is {public} and Private Key is {private}")

# Encryption function
def encrypt(plain_text):
    return (plain_text ** e) % n

# Decryption function
def decrypt(cipher_text):
    return (cipher_text ** d) % n

# Simple message to encode
msg = 9

# encrypt then decrypt
enc_msg = encrypt(msg)
dec_msg = decrypt(enc_msg)

print("Original Message:",msg)
print("Encrypted Message:",enc_msg)
print("Decrypted Message:",dec_msg)