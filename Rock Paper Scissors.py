# Samuel Hubbard
# Rock, Paper, Scissors
# Create a python code to write interactive programs of game Rock, Paper, Scissors. You(or player) and computer(or bot
# whatever you say) will play this game against each other.
# The player enters one of the words, and the computer randomly
# selects one and compares it with the player to see who wins.
# If the vocabulary entered by the player is incorrect, print： "That's not a valid play. Check your spelling!"
# If it's a draw, print: "Tie!"
# If the player lost, print: "You lose!, Paper (computer), covers, Rock (player)"
# If the player wins, print:  "You win!, Paper (player), covers, Rock (computer)"
# The "covers" can be replaced as "smashes" or "cuts" depends on the situation.

import random

while True:
    player_Move = ['Rock', 'Paper', 'Scissors']
    computer_Move = random.choice(player_Move)

    while True:
        player_Input = input("Enter your choice. Rock, Paper or Scissors \n").capitalize()
        if player_Input not in player_Move:
            print("Please enter Rock, Paper or Scissors")
        else:
            if player_Input == player_Move:
                print("It's a tie")
            elif player_Input == "Rock":
                if computer_Move == "Paper":
                    print("Paper covers Rock. You lose!")
                else:
                    print("Rock destroys scissors. You win!")
            elif player_Input == "Paper":
                if computer_Move == "Scissors":
                    print("Scissors cuts paper. You lose")
                else:
                    print("Paper covers rock. You win")
            elif player_Input == "Scissors":
                if computer_Move == "Paper":
                    print("Scissors cuts paper. You win")
                else:
                    print("Rock destroys scissors. You lose")

            replay = input("Do you want to play again? (y/n)")
            if replay.lower() == "y":
                continue
            else:
                exit()
        # finally:
            # break
