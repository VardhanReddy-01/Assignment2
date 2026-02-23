num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
add=num1+num2
sub=num1-num2
mul=num1*num2
if num2!=0:
    div=num1/num2
    mod=num1%num2
else:
    div="Cannot divide by zero"
    mod="Cannot divide by zero"
power= num1**num2
print("\nResults:")
print(num1,"+",num2,"=",add)
print(num1,"-",num2,"=",sub)
print(num1,"*",num2,"=",mul)
print(num1,"/",num2,"=",div)
print(num1,"%",num2,"=",mod)
print(num1,"^",num2,"=",power)
