num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Sorry there is no factorial for the negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("the factorial of",num,"is",factorial)
