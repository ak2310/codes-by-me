def bubble(array):
    for i in range (len(array)):
        print(array[i])
        for j in range (0,len(array)-i-1):
            if(array[j]>array[j+1]):
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp








data=[0,10,2,8,59]
bubble(data)