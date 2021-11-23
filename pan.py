pan=input("Please enter the PAN number:")
m=pan[0:5]
n=pan[5:9]
o=pan[9:10]
if len(pan)==10:
    if pan.isupper()==True and m.isalpha()==True and o.isalpha==True and n.isdigit()==True:
        print("The PAN number is valid")
    else:
        print("The PAN number is invalid")
else:
    print("The PAN number is not complete")