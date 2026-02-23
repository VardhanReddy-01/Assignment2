total=0
pass_status=True
for i in range(1, 6):
    marks=float(input("Enter marks for subject " + str(i) + ": "))
    total+=marks
    if marks<40:
        pass_status=False
    percentage=total/5
    if percentage>=90:
        grade="A+"
    elif percentage>=80:
        grade="A"
    elif percentage>=70:
        grade="B"
    elif percentage>=60:
        grade="C"
    elif percentage>=50:
        grade="D"
    else:
        grade="F"
print("Total:",total)
print("Percentage:",percentage)
print("Grade:",grade)
if pass_status:
    print("Result: PASS")
else:
    print("Result: FAIL")
