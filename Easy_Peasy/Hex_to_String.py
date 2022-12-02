
r = open("flag.txt")
r.readline()
r.readline()

flag_enc = bytearray.fromhex(r.readline()).decode()
fl = len(flag_enc)

#print(flag_enc,fl)

