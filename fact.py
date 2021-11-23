num=int(input("Please enter a number:"))
fact=1
if num<0:
    print("Factorial does not exist..")
elif num==0:
    print("Factorial is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of",num,"is",fact)