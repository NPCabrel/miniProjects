#Computer picks a random number (say between 1–20).

#User guesses until they’re correct.

#Use a loop and conditionals to guide the game (“too high”, “too low”).

import random
def number_guessing_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 20. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 20:
                print("Please guess a number within the range of 1 to 20.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
# I added error handling to manage non-integer inputs gracefully.
# I included a welcome message and instructions to enhance user experience. 
# I track the number of attempts and display it when the user guesses correctly.
# I ensured the game continues until the correct guess, providing feedback on each attempt.