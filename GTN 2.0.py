import random
import os

# User class to store user information
class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # Method to assign a score to the user
    def assignScore(self, score):
        self.score = score

    # Method to display user properties
    def displayProperties(self):
        return f"Name: {self.name}, Score: {self.score}\n"

# Function to display the title screen and handle user input
def titleScreen():
    print("---------------------------")
    print("|    NUMBER GUESSER 2.0   |")
    print("---------------------------")
    print("|     Press 1 to Play     |")
    print("|   Press 2 for Tutorial  |")
    print("| Press 3 for Leaderboard |")
    print("|     Press 4 to Exit     |")
    print("---------------------------")

    while True:
        try:
            titleInput = input("Enter your choice: ")
            if titleInput == "1":
                break
            elif titleInput == "2":
                print("Welcome to Number Guesser 2.0! The rules are simple. You have to guess the number between 1 and 100. The lower the score, the better you are! Good luck!")
                continue
            elif titleInput == "3":
                if not os.path.exists("leaderboard.txt"):
                    print("No scores yet!")
                    continue
                with open("leaderboard.txt", "r") as f:
                    print(f"\nLeaderboard:\n\n{f.read()}")
                continue
            elif titleInput == "4":
                print("Thanks for playing!")
                exit()
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to handle the game logic
def game(): 
    print("Please input a username.")
    nameInput = input()
    user = User(nameInput, 0)

    while True: 
        guessCounter = 0
        randomNumber = random.randint(1, 100)

        while True:
            userGuess = input("Enter your guess: ")

            try:
                userGuess = int(userGuess)
                if userGuess < 1 or userGuess > 100:
                    print("Guess must be between 1 and 100.")
                    continue
            except ValueError:
                print("Guess must be a number between 1 and 100.")
                continue

            guessCounter += 1

            if userGuess > randomNumber:
                print("Guess is too high!")
            elif userGuess < randomNumber:
                print("Guess is too low!")
            else:
                print("That's correct!")
                print(f"You guessed the number in {guessCounter} tries.")

                finalScore = guessCounter * 100
                user.assignScore(finalScore) 

                with open("leaderboard.txt", "a") as f:  
                    f.write(user.displayProperties())  

                print(f"Your score is {finalScore} and has been saved to 'leaderboard.txt'.")

                sortScores()
                break

        while True:
            gameInput = input("Would you like to play again? (Y/N): ").strip().capitalize()
            if gameInput == "Y":
                 break  
            elif gameInput == "N":
                print("Thanks for playing!")
                return 
            else:
                print("Invalid Input. (Y/N) only.")
                continue

# Function to sort scores in the leaderboard
def sortScores():
    if not os.path.exists("leaderboard.txt"):  
        open("leaderboard.txt", "w").close() 
        return  

    with open("leaderboard.txt", "r") as f: 
        lines = f.readlines()

    users = []
    for line in lines:
        parts = line.strip().split(", ")
        if len(parts) == 2 and "Name: " in parts[0] and "Score: " in parts[1]:  
            name = parts[0].split(": ")[1] 
            userscore = parts[1].split(": ")[1] 

            if userscore.isdigit():  
                users.append((name, int(userscore))) 

    users.sort(key=lambda x: x[1])  
    with open("leaderboard.txt", "w") as f:
        for user in users:
            f.write(f"Name: {user[0]}, Score: {user[1]}\n")
        f.write("\nThe lower the score, the better you are!\n")

# Display the title screen and start the game
titleScreen()
game()
