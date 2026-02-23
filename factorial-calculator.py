n=int(input("Enter a number: "))
if n<0:print("Not defined")
elif n==0:print("0! = 1")
else:
    f=1
    print(str(n)+"! =",end=" ")
    for i in range(n,0,-1):
        print(i,end="")
        f*=i
        if i>1:print(" × ",end="")
    print(" =",f)