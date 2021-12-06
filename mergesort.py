from array import array


def ms(array):
    if len(array)>1:
        mid=len(array)//2
        L=array[:mid]
        R=array[mid:]
        ms(L)
        ms(R)

        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                array[k]=L[i]
                i +=1
            else:
                array[k]=R[j]
                j+=1
            k+=1
        
        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            array[k]=R[j]
            j+=1
            k+=1

def printlist(array):
    for i in range(len(array)):
        print(array[i],end=" ")
    print()

if __name__=='__main__':
    array=[12,58,96,3,57]
    print("Given array is",end="\n")
    printlist(array)
    ms(array)
    print("Sorted array is:",end="\n")
    printlist(array)