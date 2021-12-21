import re
string="This is python class"
result=re.findall('python',string)
print(result)

### re in phone number

string=input()
pattern='(0|+91)?[1-9][0-9]{9}'
if re.match(pattern,string):
    print("Valid")
else:
    print("Invalid")