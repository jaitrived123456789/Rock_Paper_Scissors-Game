import random
def Get_choices():
    player_choice=input("Enter the choice(rock,paper,sissors):")
    options=["rock","paper","sissors"]
    computer_choice=random.choice(options)
    choice={"player":player_choice,"computer":computer_choice}
    return choice
def Get_win(player,computer):
    
    if player==computer:
        print(f"you choose {player} computer choose {computer}:\n")
        print("Its a tie!")

    elif player=="paper":
        if computer=="sissors":
            print(f"you choose {player} computer choose {computer}:")
            print("You Loose")
        else:
            print(f"you choose {player} computer choose {computer}:")
            print("You Win")

    elif player=="rock":
        if computer=="sissors":
            print(f"you choose {player} computer choose {computer}:")
            print("You Win")
        else:
            print(f"you choose {player} computer choose {computer}:")
            print("You Loose")

    elif player=="sissors":
        if computer=="rock":
            print(f"you choose {player} computer choose {computer}:")
            print("You Loose")
        else:
            print(f"you choose {player} computer choose {computer}:")
            print("You Win")

choices=Get_choices()
Get_win(choices["player"],choices["computer"])


