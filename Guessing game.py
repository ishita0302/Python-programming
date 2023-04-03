import random
n = random.randint(1, 10)
while True:
    s = int(input("enter number from 1 to 9: "))
    if s < n:
        print("too low.")
    elif s > n:
        print("too high.")
    else:
        print("you won.")
        p = input("do you want to play again (y/n): ")
        if p == "y":
            n = random.randint(1, 10)
        else:
            break