t=input("Enter word/number: ")
r=t[::-1]
print("Original:",t)
print("Reversed:",r)
print("Result:","PALINDROME" if t.lower()==r.lower() else "NOT PALINDROME")