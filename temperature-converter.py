print("1.C to F")
print("2.F to C")
print("3.C to K")
print("4.K to C")
print("5.F to K")
print("6.K to F")
print("7.Exit")
choice=int(input("Enter choice: "))
if choice==1:
    c=float(input("Enter Celsius: "))
    print("Fahrenheit:",(c*9/5)+32)
elif choice==2:
    f=float(input("Enter Fahrenheit: "))
    print("Celsius:",(f-32)*5/9)
elif choice==3:
    c=float(input("Enter Celsius: "))
    print("Kelvin:",c+273.15)
elif choice==4:
    k=float(input("Enter Kelvin: "))
    print("Celsius:",k-273.15)
elif choice==5:
    f=float(input("Enter Fahrenheit: "))
    print("Kelvin:",(f-32)*5/9+273.15)
elif choice==6:
    k=float(input("Enter Kelvin: "))
    print("Fahrenheit:",(k-273.15)*9/5+32)
elif choice==7:
    print("Exiting")
else:
    print("Invalid choice")