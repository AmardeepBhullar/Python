# Printing prime numbers using for else statement
num = 403
if num == 1:
    print(num,"Thia is not a prime number")
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"This is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num, "This is a prime number")
else:
    print(num,"This is not a prime number")
