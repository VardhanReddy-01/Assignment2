age=int(input("Enter age: "))
day=input("Enter day: ").lower()
tickets=int(input("Enter number of tickets: "))
if age<3:price=0
elif age<=12:price=150
elif age<=59:price=300
else:price=200
base=price*tickets
if day in["friday","saturday","sunday"]:discount=base*0.2
else:discount=0
after=base-discount
print("Price per ticket:",price)
print("Base price:",base)
print("Discount:",discount)
print("Price after discount:",after)
print("Total amount:",after)