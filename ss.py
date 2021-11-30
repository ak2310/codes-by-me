def ss(array):
    for i in range(len(array)):
        min=i
        for j in range(i+1,len(array)):
            if (array[min]>array[j]):
                min=j
        array[i],array[min]=array[min],array[i]
        print(array)

array=[67,77,2,54,89,11,7]
ss(array)
print(array)