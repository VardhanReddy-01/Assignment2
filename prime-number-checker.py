n=int(input("Enter a number: "))
if n<=1:print("Not prime")
else:
    prime=True
    for i in range(2,n):
        if n%i==0:prime=False
    if prime:print("Prime number")
    else:print("Not prime")

s=int(input("Enter start range: "))
e=int(input("Enter end range: "))
print("Prime numbers:",end=" ")
for x in range(s,e+1):
    if x>1:
        prime=True
        for i in range(2,x):
            if x%i==0:prime=False
        if prime:print(x,end=" ")