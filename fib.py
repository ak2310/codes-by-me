n=int(input("Please enter a number:"))
n1,n2=0,1
cnt=0
if n<=0:
    print("Please enter a positive number..")
elif n==0:
    print(n1)
else:
    while cnt<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        cnt+=1