def binarysearch(array,l,r,x):
    if r>=l:
        md=l+(r-1)//2
        if array[md]==x:
            return md
        elif array[md]>x:
            return binarysearch(array,l,md-1,x)
        else:
            return binarysearch(array,md+1,r,x)
    else:
        return -1

array=[1,9,87,100,25,6]
x=1

r=binarysearch(array,0,len(array)-1,x)
if r==-1:
    print("Element not found")
else:
    print("Element is present in index",r)