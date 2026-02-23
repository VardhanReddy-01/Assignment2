n=int(input("Enter Number: "))
r=int(input("End Range: "))
print("Multiplication Table of",n)
for i in range(1,r+1):
    print(n,"x",i,"=",n*i)