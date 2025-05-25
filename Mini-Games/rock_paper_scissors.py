import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

while True:
    player_pick = input("Please pick: 'Rock', 'Paper' or 'Scissors' ") # Ask input from user - Rock, Paper or Scissors

    if player_pick != rock and player_pick != paper and player_pick != scissors:
        print("Incorrect choice! Please start again.")
        break

    computer_random = random.randint(1, 3)  # Generate random pick from computer
    computer_pick = ""

    if computer_random == 1:
        computer_pick = "Rock"
    elif computer_random == 2:
        computer_pick = "Paper"
    elif computer_random == 3:
        computer_pick = "Scissors"

    print(f"Your pick is: {player_pick}")   # Show both player and computer picks
    print(f"Computer pick is: {computer_pick}")

    # Logic of the game:
    if player_pick == "Rock" and computer_pick == "Scissors":
        print("You win!")
        break
    elif player_pick == "Paper" and computer_pick == "Rock":
        print("You win!")
        break
    elif player_pick == "Scissors" and computer_pick == "Paper":
        print("You win!")
        break
    elif player_pick == computer_pick:
        print("It's a draw!")
        break
    else:
        print("You lost!")
        break
