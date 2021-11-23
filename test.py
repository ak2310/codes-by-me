balance=float(input("Please enter balance:")
print("M/F:")
g=input()
if balance>5000 and g=="F":
    nb=balance+(5*balance)/100
else:
    nb=balance+(2*balance)/100
print(nb)