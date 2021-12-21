f=open('ak.txt','w')
a=input()
f.write(a)
f.close()
f=open('ak.txt','r')
str=f.read()
print(str)
f.close()

#a-append
#r-read
#w-write
#w+
#r+
#a+
#x
