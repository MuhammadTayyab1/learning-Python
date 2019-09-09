import random

num=random.randint(1,10)

for i in range(5):
    user=int(input("Enter number b/w 1-10"))
    if user==num:
        print("You win")
        break
    elif user<num:
        print("Too low")
        continue
    elif user>num:
        print("Too high")
        continue

