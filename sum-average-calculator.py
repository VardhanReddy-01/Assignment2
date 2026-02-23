c=int(input("How many numbers? "))
nums=[]
for i in range(1,c+1):
    nums.append(float(input("Enter number "+str(i)+": ")))
s=sum(nums)
print("Sum:",s)
print("Average:",s/c)
print("Maximum:",max(nums))
print("Minimum:",min(nums))