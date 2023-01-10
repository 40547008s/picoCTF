The key point to decode is to nuderstand the encode

look at the new_caesar.py
we can find the encode function are b16_encode and shift

b16_encode() is to split a char (one byte) to two byte.
char to binary array : "{0:08b}".format(ord(c))
split a byte to two  : ALPHABET[int(binary[:4],2)] #the front 4 bit
split a byte to two  : ALPHABET[int(binary[4:],2)] #the back 4 bit

shift(c,k) is to c+k and mapping to 0~15 (4 bit length)
char to int (0~15) convertion :t1 = ord(c) - LOWERCASE_OFFSET
char to int (0~15) convertion :t2 = ord(k) - LOWERCASE_OFFSET
clock within 0~15 : (t1+t2) % len(ALPHABET)

In order to reverse the coding, we need to reverse the shit first.

reverse shift function : enc - key + LOWERCASE_OFFSET
there are two case {enc > key} or {enc < key}
if case one : plain = enc - key + LOWERCASE_OFFSET
if case two : plain = enc - key + 16 + LOWERCASE_OFFSET #transfor the minus num to the range 0~15

and we can brute force the key (0~15 index of ALPHABET)
for k in range(len(ALPHABET)):
    for i in enc:
        index = ALPHABET.index(i) #convert char to int (0~15)
        if(k <= index):
            b16[k] += chr(index - k + LOWERCASE_OFFSET)
        else:
            b16[k] += chr(index - k + 16 + LOWERCASE_OFFSET)

and then to combine the plain text for each two element.
for k in range(len(ALPHABET)):
    flag = ""
    p = plain[k]
    for i in range(0, len(p), 2):
        index1 = ALPHABET.index(p[i])
        index2 = ALPHABET.index(p[i+1])
        flag += chr((index1 << 4) + index2)
    print(flag)

Last to find out the most likely string of the flag and try to submit it.
Remember to add with picoCTF{<flag>}

