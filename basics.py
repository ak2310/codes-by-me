age = int(input("Enter your age:"))
if age > 18:
    print("You are eligible to vote")
elif age==18:
    print("All the best for your first vote")
else:
    age_ = 18-age
    print("You need to wait for", age_, "years to vote")

#%%
num=int(input("Please enter the number to check:"))
if num%2==0:
    print("This is an even number...")
else:
    print("The given number is odd...")