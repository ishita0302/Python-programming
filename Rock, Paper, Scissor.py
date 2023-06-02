import random
print("Game: rock, paper, scissor")
s = input("press 1 if you want to play with computer and 0 if you dont: ")

if s == 0:
    p1 = input("player 1:")
    p2 = input("player 2:")
    if p1 == p2:
        print("tie!")
    elif p1 == "rock" and p2 == "scissors":
        print("player1 wins")
    elif p1 == "paper" and p2 == "rock":
        print("player1 wins")
    elif p1 == "scissors" and p2 == "paper":
        print("player1 wins")
    else:
        print("player2 wins")

else:
    p1 = input("your turn:")
    c = random.randint(1, 3)
    if c == 1:
        p2 = "rock"
        print(f"computer move: {p2}")
    elif c == 2:
        p2 = "paper"
        print(f"computer move: {p2}")
    else:
        p2 = "scissor"
        print(f"computer move: {p2}")

    if p1 == p2:
        print("tie!")
    elif p1 == "rock" and p2 == "scissors":
        print("you win")
    elif p1 == "paper" and p2 == "rock":
        print("you win")
    elif p1 == "scissors" and p2 == "paper":
        print("you win")
    else:
        print("computer wins")