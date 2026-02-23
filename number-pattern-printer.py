print("1.Pattern1 2.Pattern2 3.Pattern3 4.Pattern4")
c=int(input("Choice: "))
h=int(input("Height: "))
if c==1:
    for i in range(1,h+1):
        for j in range(1,i+1):print(j,end=" ")
        print()
elif c==2:
    for i in range(1,h+1):
        for j in range(i):print(i,end=" ")
        print()
elif c==3:
    for i in range(h,0,-1):
        for j in range(i,0,-1):print(j,end=" ")
        print()
elif c==4:
    for i in range(1,h+1):
        print(" "*(h-i),end="")
        for j in range(1,i+1):print(j,end="")
        for j in range(i-1,0,-1):print(j,end="")
        print()
else:print("Invalid")