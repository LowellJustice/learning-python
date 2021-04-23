import random


def userInput():
    response = input("Would you like to play again? Type \'1\' for yes and" +
                     "\'2\' for no: ")
    if response.strip() != '1' and response.strip() != '2':
        print("Did not respond with a one or a two. Try again.")
        userInput()

    if response.strip() == '1':
        playGame()


def playGame():
    value = input("Write \'rock\', \'paper\', or \'scissors\' to play: ")
    value = value.strip().lower()
    if (value != "rock" and value != "paper"
            and value != "scissors"):
        playGame()

        computerMove = random.randint(1, 3)
        if computerMove == 1:
            if value == "rock":
                print("We both played rock! It's a draw")
                userInput()
            elif value == "paper":
                print("I played rock and you played paper! Looks like you" +
                      "win!")
                userInput()
            else:
                print("You played scissors, I played rock. I win!")
                userInput()
        elif computerMove == 2:
            if value == "rock":
                print("You played rock and I played paper! I win.")
                userInput()
            elif value == "paper":
                print("We both played paper! Again?")
                userInput()
            else:
                print("You played scissors, I played paper. Dang it! You win.")
                userInput()
        else:
            if value == "rock":
                print("You played rock and I played scissors! You win.")
                userInput()
            elif value == "paper":
                print("I played scissors and you played paper! I win!")
                userInput()
            else:
                print("You played scissors, I played scissors. Again?")
                userInput()


playGame()
