from factordb.factordb import FactorDB
import gmpy2

with open('values') as f:
    lines = f.readlines()
    c = int(lines[1][2:])
    n = int(lines[2][2:])
    e = int(lines[3][2:])

f = FactorDB(n)
f.connect()
p, q = f.get_factor_list()
ph = (p-1) * (q-1)
d = gmpy2.invert(e,ph)
plaintext = pow(c, d, n)
print("Flag: {}".format(bytearray.fromhex(format(plaintext, 'x')).decode()))

