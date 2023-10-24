import random


def game():
    playerp = 0
    computerp = 0
    while playerp < 3 or computerp < 3:
        user_action = input("\nEnter rock, paper or scissors: ")
        possible_actions = ("rock", "paper", "scissors")

        computer = random.choice(possible_actions)
        print("You chose: ", user_action, "\ncomputer chose:", computer, "\n")

        if user_action == computer:
            print("Both players selected", user_action, "It's a tie!\n Both of you earned a point!!\n")
            playerp = playerp + 1
            computerp = computerp + 1

        elif user_action == "rock":
            if computer == "scissors":
                print(" You win!\n You Earned 1 point")
                playerp = playerp + 1
            else:
                print(" You lose.\n The computer earned 1 point!!")
                computerp = computerp + 1

        elif user_action == "paper":
            if computer == "rock":
                print(" You win!\n You Earned 1 point")
                playerp = playerp + 1
            else:
                print(" You lose.\n The computer earned 1 point!!")
                computerp = computerp + 1

        elif user_action == "scissors":
            if computer == "paper":
                print(" You win!\n You Earned 1 point")
                playerp = playerp + 1
            else:
                print(" You lose.\n The computer earned 1 point!!")
                computerp = computerp + 1

        if playerp == (3):
            print("You Won The Game!")
            break

        if computerp == (3):
            print("Wow you really lost to a computer")
            break


game()