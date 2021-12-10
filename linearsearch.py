def search(array,x):
    for i in range(len(array)):
        if array[i]==x:
            return i
    return -1
array=[1,9,8,6,85,20]
x=1


result=search(array,x)
if(result==-1):
    print("Element not present in the array")
else:
    print("Element is present in the array at",result)