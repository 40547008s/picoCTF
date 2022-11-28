def egcd(a,b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b//a)*y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
with open('values') as f:
    lines = f.readlines()
p = 24347923845234843815836340424784150579611
q = 6508096157420555814598202533569873963460631

n = int(lines[2][3:])
phi = (p-1) * (q-1)
e = int(lines[3][3:])
d = modinv(e, phi)
c = int(lines[1][3:])


plain = pow(c, d, n)
print(plain)
print(hex(plain))
print(bytearray.fromhex(hex(plain)[2:]))
print(bytearray.fromhex(format(plain, 'x')).decode("utf-8","ignore"))

