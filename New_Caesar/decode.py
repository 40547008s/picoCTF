import string
ALPHABET = string.ascii_lowercase[:16]

b16 = [""]*len(ALPHABET)
print(b16)
enc = input()
for i in enc:
    for k in range(len(ALPHABET)):
        index = ALPHABET.index(i)
        if(k <= index):
            if(index -k+97 > 127): break
            b16[k]+=chr(index -k+97)
        else:
            if(index +16-k+97 > 127): break
            b16[k]+=chr(index +16-k+97)

for k in range(len(ALPHABET)):
    flag=""
    b = b16[k]
    for i in range(0, len(b), 2):
        if(b[i+1] in ALPHABET and b[i] in ALPHABET):
            index1 = ALPHABET.index(b[i])
            index2 = ALPHABET.index(b[i+1])
            flag+= chr((index1 <<4) +index2)
    print(flag)