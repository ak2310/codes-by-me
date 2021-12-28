m=int(input('Enter the number of lists: '))
n=int(input('Enter the lenth of list: '))

rows, cols = (m,n)
arr=[]
for i in range(rows):
    column = []
    for j in range(cols):
        column.append(input('Enter the element to append in the list: '))
    print('list')
    arr.append(column)
print(arr)

p=int(input('Index of primary key: '))
pq=input('Primary key query: ')


sp1=arr[0]
sp2=arr[1]

if sp1[p]==str(pq):
    print(sp1)
else:
    print(sp2)