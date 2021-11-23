#Program to store marks in an array and find sum and average
from array import*
#accept marks as a string
#list is a datatype derived from array
#array is continuous storage of similar data
str=input("Enter the marks:").split(' ')
print(type(str))
marks=[int(num) for num in str]
print(marks)
sum=0
for x in marks:
    sum=sum+x
print("sum of the marks is:",sum)
avg=sum/len(marks)
print(avg)

