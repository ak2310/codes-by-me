nterms=int(input())
n1=0
n2=1
count=0
while(count<nterms):
    print(n1)
    nth=n1+n2
    n1=n2 #updating the next value
    n2=nth #updating next value
    count=count+1
