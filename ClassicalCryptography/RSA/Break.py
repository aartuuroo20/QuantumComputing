n = 247  # the modulus
e = 5    # public key number
a = 6    # an integer coprime to n
assert gcd(a, n) == 1
print(f"Checked {n} and {a} are coprime")

r=0
rem = 100
while(rem != 1):
    r += 1
    rem = (a**r) % n
    
print(f'period r is: {r}')
assert a**r % n == 1

print(f"Checked {a}^{r} mod {n} is 1")

# explicitly use as integer
f1 = int ( a**(r/2) - 1)
f2 = int ( a**(r/2) + 1)

print(f"f1 = {f1}")
print(f"f2 = {f2}")

q_found = gcd(f1, n)
print(f'One possible prime factor of n ({n}) is: {q_found}')

# explicit int (to avoid floating point)
p_found = int ( n/q_found )
print(f'The second prime factor of n ({n}) is: {p_found}')

assert n == p_found * q_found

#Compute the totient
phi_found = ( p_found -1 ) * ( q_found - 1 ) 
print(f'The totient is: {phi_found}')

#Recover the private key number d_found by satisfying (d_found * e) % phi_found = 1
d_found = 1
while(True):
    if((d_found*e) % phi_found == 1):
        break
    else:
        d_found += 1
print("Private Key number (d_found):",d_found)