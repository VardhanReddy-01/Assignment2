def factorial(n):
    f=1
    for i in range(1,n+1):f*=i
    return f

def is_prime(n):
    if n<=1:return False
    for i in range(2,n):
        if n%i==0:return False
    return True

def fibonacci(n):
    a,b=0,1
    for i in range(n):a,b=b,a+b
    return a

def sum_of_digits(n):return sum(int(d) for d in str(n))

def reverse_number(n):return int(str(n)[::-1])

def is_armstrong(n):
    p=len(str(n))
    return sum(int(d)**p for d in str(n))==n

def gcd(a,b):
    while b:a,b=b,a%b
    return a

def lcm(a,b):return a*b//gcd(a,b)

def is_perfect_number(n):
    s=0
    for i in range(1,n):
        if n%i==0:s+=i
    return s==n

def math_menu():
    while True:
        print("1.Fact 2.Prime 3.Fibo 4.SumDigits 5.Rev 6.Arm 7.GCD 8.LCM 9.Perfect 10.Exit")
        c=input()
        if c=="10":break
        if c in["7","8"]:
            a=int(input("Enter a: "))
            b=int(input("Enter b: "))
        else:n=int(input("Enter n: "))
        if c=="1":print(factorial(n))
        elif c=="2":print(is_prime(n))
        elif c=="3":print(fibonacci(n))
        elif c=="4":print(sum_of_digits(n))
        elif c=="5":print(reverse_number(n))
        elif c=="6":print(is_armstrong(n))
        elif c=="7":print(gcd(a,b))
        elif c=="8":print(lcm(a,b))
        elif c=="9":print(is_perfect_number(n))

math_menu()