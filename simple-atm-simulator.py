balance=10000
while True:
    print("1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    choice=input("Enter choice: ")
    if choice=="1":print("Balance:",balance)
    elif choice=="2":
        amount=float(input("Enter amount to deposit: "))
        balance+=amount
        print("Deposit successful!")
        print("New balance:",balance)
    elif choice=="3":
        amount=float(input("Enter amount to withdraw: "))
        if amount<=balance-500:
            balance-=amount
            print("Withdrawal successful!")
            print("New balance:",balance)
        else:print("Insufficient balance! Minimum ₹500 must remain.")
    elif choice=="4":break
    else:print("Invalid choice")