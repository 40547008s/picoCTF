alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cyber = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
nums = cyber.split()
decode = [ alpha[int(i)-1] if i != '{' and i != '}' else i for i in nums]
print(decode)
plaintext = ""
for i in decode:
    plaintext += i
print(plaintext)