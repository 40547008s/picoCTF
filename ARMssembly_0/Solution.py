a = input("Please give me two numbers >>>").split(' ')
num1, num2 = int(a[0]), int(a[1])
print("{:x}".format(num1),"{:x}".format(num2))
bigger = num1 if num1 > num2 else num2
print("picoCTF{" + "{:x}".format(bigger) + "}") 