def part(array,low,high):
    i=(low-1)
    pivot=array[high]
    
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return(i+1)

def qs(array,low,high):
    if len(array)==1:
        return array
    if low<high:
        pi=part(array,low,high)
        qs(array,low,pi-1)
        qs(array,pi+1,high)
array=[1,87,63,85,9,2,999]
n=len(array)
qs(array,0,n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % array[i])