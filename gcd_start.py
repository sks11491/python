def gcd(a, b):
    a, b = int(a), int(b)
    if a < b:
        c = a
        a = b
        b = c
    while( b != 0):
        c = a
        a = b
        b = c % b
    return a

a = input("Enter A:")
b = input("Enter B:")
print("GCD : ", gcd(a, b))
