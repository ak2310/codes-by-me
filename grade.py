mark=int(input("Enter your marks:"))
if (mark>100):
    print("Please enter a valid mark...")
elif (mark>90 and mark<=100):
    print("A+ Grade")
elif (mark>80 and mark<90):
    print("B Grade")
elif (mark>70):
    print("C Grade")
elif (mark>50):
    print("D Grade")
else:
    print("Better luck next time")