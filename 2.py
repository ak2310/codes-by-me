n=int(input('Enter the number of lists: '))
M=int(input('Enter the lenth of list: '))

rows, cols = (2,M)
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(input('Enter the element to append in the list: '))
    print('list')
    arr.append(col)
print(arr)

p=int(input('Enter the index of primary key: '))
pq=input('Enter the primary ket query: ')


split1=arr[0]
split2=arr[1]

if split1[p]==str(pq):
    print(split1)
else:
    print(split2)