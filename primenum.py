# Printing prime number using flag variable statement
num = 30
flag = False
if num == 1:
    print(num, "this is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, "this is not a prime number")
    else:
        print(num,"this is a prime number")
