# Samuel Hubbard
#Rock, Paper, Scissors
#Create a python code to write interactive programs of game Rock, Paper, Scissors. You(or player) and computer(or bot
# whatever you say) will play this game against each other. The player enters one of the words, and the computer randomly
#selects one and compares it with the player to see who wins.
#If the vocabulary entered by the player is incorrect, print： "That's not a valid play. Check your spelling!"
#If it's a draw, print: "Tie!"
#If the player lost, print: "You lose!, Paper (computer), covers, Rock (player)"
#If the player wins, print:  "You win!, Paper (player), covers, Rock (computer)"
#The "covers" can be replaced as "smashes" or "cuts" depends on the situation.
import random

move_list = ['Rock', 'Paper', 'Scissors']
move = random.choice(move_list)


if __name__ == '__main__':

    print("Let's play rock paper scissors")
