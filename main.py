from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random number to the computer
computer = t[randint(0,2)]

#score declaration
score = 0
#determines who wins and loses
result = False
#player as false to keep loop going
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        result = False
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            result = False
            print("You lose!", computer, "covers", player)
        else:
            result = True
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            result = False
            print("You lose!", computer, "cut", player)
        else:
            result = True
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            result = False
            print("You lose...", computer, "smashes", player)
        else:
            result = True
            print("You win!", player, "cut", computer)
    else:
        result = False
        print("That's not a valid play. Check your spelling!")

#player set to false so the loop continues
    player = False
    computer = t[randint(0,2)]

# if statement to get and set score
    if result == True:
      score += 1
      print(score)
    else:
      print(score)
