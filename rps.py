def rockpaperscissors(plyr1,plyr2):
    if plyr1 == "rock" and plyr2 == "rock":
        print("tie!")
    if plyr1 == "rock" and plyr2 == "scissors":
        print("player 1 wins!")
    if plyr1 == "rock" and plyr2 == "paper":
        print("player 2 wins!")
    if plyr1 == "scissors" and plyr2 == "scissors":
        print("tie!")
    if plyr1 == "scissors" and plyr2 == "paper":
        print("player 1 wins!")
    if plyr1 == "scissors" and plyr2 == "rock":
        print("player 2 wins!")
    if plyr1 == "paper" and plyr2 == "paper":
        print("tie!")
    if plyr1 == "pape"r and plyr2 == "rock":
        print("player 1 wins!")
    if plyr1 == "paper" and plyr2 == "scissors":
        print("player 2 wins!")





if __name__ == "__main__":
    skib1 = input("rock, paper, or scissors?")
    skib2 = input("rock, paper, or scissors?")
    rockpaperscissors(skib1,skib2)