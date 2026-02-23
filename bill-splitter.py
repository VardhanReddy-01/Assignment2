bill=float(input("total bill: "))
people=int(input("number of people: "))
tax_percent=float(input("tax percentage: "))
tip_percent=float(input("tip percentage: "))
tax=bill*tax_percent/100
after_tax=bill+tax
tip=after_tax*tip_percent/100
total=after_tax+tip
per_person=total/people
print("\n=== BILL BREAKDOWN ===")
print("Subtotal:₹",bill)
print("Tax:₹",tax)
print("After tax:₹",after_tax)
print("Tip:₹",tip)
print("Total:₹",total)
print("Per person:₹",per_person)
