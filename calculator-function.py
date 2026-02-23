def add(a,b):return a+b
def subtract(a,b):return a-b
def multiply(a,b):return a*b
def divide(a,b):return "Zero error" if b==0 else a/b
def modulus(a,b):return a%b
def power(a,b):return a**b

def calculator():
    while True:
        print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus 6.Power 7.Exit")
        c=input("Choice: ")
        if c=="7":break
        a=float(input("Enter first: "))
        b=float(input("Enter second: "))
        if c=="1":print(add(a,b))
        elif c=="2":print(subtract(a,b))
        elif c=="3":print(multiply(a,b))
        elif c=="4":print(divide(a,b))
        elif c=="5":print(modulus(a,b))
        elif c=="6":print(power(a,b))

calculator()