import re
na=input()

age=re.findall(r'\d{1,3}',na)
name=re.findall(r'[A-Z][a-z]*',na)

agedict={}
if len(name)==0 or len(age)==0:
    print('input empty')
else:
    for i in range(len(name)):
        f={name[i]:age[i]}
        agedict.update(f)
    print(agedict)