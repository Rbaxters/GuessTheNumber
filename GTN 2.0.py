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
                break  # Exit the loop to start the game
            elif titleInput == "2":
                print("Welcome to Number Guesser 2.0! The rules are simple. You have to guess the number between 1 and 100. The lower the score, the better you are! Good luck!")
                continue  # Display the tutorial and continue the loop
            elif titleInput == "3":
                if not os.path.exists("leaderboard.txt"):
                    print("No scores yet!")
                    continue  # If leaderboard file doesn't exist, continue the loop
                with open("leaderboard.txt", "r") as f:
                    print(f"\nLeaderboard:\n\n{f.read()}")
                continue  # Display the leaderboard and continue the loop
            elif titleInput == "4":
                print("Thanks for playing!")
                exit()  # Exit the program
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to handle the game logic
def game(): 
    print("Please input a username.")
    nameInput = input()
    user = User(nameInput, 0)  # Create a new user with the provided username

    while True: 
        guessCounter = 0  # Initialize guess counter
        randomNumber = random.randint(1, 100)  # Generate a random number between 1 and 100

        while True:
            userGuess = input("Enter your guess: ")

            try:
                userGuess = int(userGuess)
                if userGuess < 1 or userGuess > 100:
                    print("Guess must be between 1 and 100.")
                    continue  # If guess is out of range, continue the loop
            except ValueError:
                print("Guess must be a number between 1 and 100.")
                continue  # If input is not a valid number, continue the loop

            guessCounter += 1  # Increment guess counter

            if userGuess > randomNumber:
                print("Guess is too high!")
            elif userGuess < randomNumber:
                print("Guess is too low!")
            else:
                print("That's correct!")
                print(f"You guessed the number in {guessCounter} tries.")

                finalScore = guessCounter * 100  # Calculate the final score
                user.assignScore(finalScore)  # Assign the score to the user

                # Append the user's score to the leaderboard file
                with open("leaderboard.txt", "a") as f:  
                    f.write(user.displayProperties())  

                print(f"Your score is {finalScore} and has been saved to 'leaderboard.txt'.")

                sortScores()  # Sort the scores in the leaderboard
                break  # Exit the inner loop to ask if the user wants to play again

        while True:
            gameInput = input("Would you like to play again? (Y/N): ").strip().capitalize()
            if gameInput == "Y":
                break  # Break the loop to start a new game
            elif gameInput == "N":
                print("Thanks for playing!")
                return  # Exit the game function
            else:
                print("Invalid Input. (Y/N) only.")
                continue  # If input is invalid, continue the loop

# Function to sort scores in the leaderboard
def sortScores():
    if not os.path.exists("leaderboard.txt"):  
        open("leaderboard.txt", "w").close()  # Create the leaderboard file if it doesn't exist
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
                users.append((name, int(userscore)))  # Add valid user scores to the list

    users.sort(key=lambda x: x[1])  # Sort users by score in ascending order
    with open("leaderboard.txt", "w") as f:
        for user in users:
            f.write(f"Name: {user[0]}, Score: {user[1]}\n")
        f.write("\nThe lower the score, the better you are!\n")  # Add a note at the end of the file

# Display the title screen and start the game
titleScreen()
game()

