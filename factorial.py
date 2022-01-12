def fact():
    num=int(input())
    fact=1
    if num<0:
        print("Factorial does not exist for negative numbers..")
    elif num==0:
        print("Factorial is 1")
    else:
        for i in range(1,num+1):
            fact=fact*1
            print("Factorial of %d is %d"%(i,fact))
        print("Factorial of %d is %d"%(i,fact))

#def fact(n):
    fact=1
    while(n>=1):
        fact=fact*n
        n=n-1
    return fact
#for i in range(1,n+1):
    #print("Factorial of {} is {}".format(i,fact(i)))
