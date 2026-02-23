import random
num=random.randint(1,100)
a=7
while a>0:
    g=int(input("Guess: "))
    if g==num:
        print("Correct!")
        break
    elif g>num:print("Too high")
    else:print("Too low")
    a-=1
    print("Attempts left:",a)
if a==0:print("Game over. Number was:",num)