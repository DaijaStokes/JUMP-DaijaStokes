player_one=input("Player One: Please enter rock,R, paper,P, or scissors,S: ")
player_two=input("Player Two: Please enter rock,R, paper,P, or scissors,S: ")

if player_one == player_two:
    print(f"Both players selected {player_one}. It's a tie!")
elif player_one == "R":
    if player_two == "S":
        print("Rock wins!")
    else:
        print("Paper wins!")
elif player_one == "P":
    if player_two == "R":
        print("Paper wins!")
    else:
        print("Scissors wins!")
elif player_one == "S":
    if player_two == "P":
        print("Scissors wins!")
    else:
        print("Rock wins!")