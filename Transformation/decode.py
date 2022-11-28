
with open('enc') as f:
    flag = f.readlines()
    print(flag[0].encode('utf-16-be'))
    #print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i+1])) for i in range(0, len(flag), 2)]))

