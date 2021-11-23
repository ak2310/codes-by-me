x=[]
for i in range(1,26):
    m=int(input("Please enter the mark:"))
    x.append(m)
sum_=sum(x)
avg=sum_/len(x)
print("Average of the given marks is ",avg)
