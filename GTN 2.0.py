import random
import os

class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def assignScore(self, score):
        self.score = score

    def displayProperties(self):
        return f"Name: {self.name}, Score: {self.score}\n"

def titleScreen():
    print("---------------------------")
    print("|    NUMBER GUESSER 2.0   |")
    print("---------------------------")
   
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

titleScreen()
game()