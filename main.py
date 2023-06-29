import random
def get_choices():

    player_choice = input("Enter your choice (rock, paper, scissors) : ")
    computer_option = ["rock","paper","scissors"]
    computer_choice = random.choice(computer_option)
    choices = {"player": player_choice, "computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"player choice {player} , computer choice {computer}")
    if player == computer :
        return "it's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashed the scissors! you win!"
        else:
            return "paper cover rock! you lose!"

    elif player == "scissors":
        if computer == "paper":
            return "scissors cut the paper! you win!"
        else:
            return "rock smashes the scissors! you lose!"

    elif player == "paper":
        if computer == "scissors":
            return "scissors cut the paper! you lose!"
        else:
            return "paper cover rock!  you win!"


choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)