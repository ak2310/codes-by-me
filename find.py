from array import *
a=array('i',[])
n=int(input("Enter the number of integers:"))
for i in range(n):
    a.append(int(input()))
print(a)
a.append(int(input("enter a number to be added:")))
print(a)
print(sorted(a))
#function to sort the elements
a.remove(int(input("enter the number to be removed:")))
#function to remove an element
print(a)
print(len(a))
#function to find the length of the array
(min(a))
#function that shows the lowest element of the array
print(a.count(40))
#function that counts the number of repeatation of an element in the array
a.reverse()
#function to reverse the array
print(a)
print(sum(a))
#function that displays the sum of the entire array
a.insert(2,25)
#function that adds an element at a given location in the array
print(a)
b=array('i',[69,58,69,7])
a.extend(b)
#function that adds another list to the current list
print(a)
print(max(a))
#function that displays the largest element in the given array
