
# Name: Nwobi Golibe
# This is a program that gives the user a chance to guess a number between 1 and 10.
# The computer randomly chooses the number, and the user is told whether their guess is too high or too low.
# Once the correct number is guessed, the program congratulates the user and tells them how many attempts it took.

import random  # We need this to generate random numbers

# Step 1: The computer picks a random number between 1 and 10
print("I'm thinking of a number between 1 and 10.")
computer_choice = random.randint(1, 10)

# Step 2: Initialize the guess counter
number_of_guesses = 0

# Step 3: Set the initial guess to something that's not the correct answer
guess_of_user = -1  # This ensures the loop starts

# Step 4: Keep asking the user until they guess correctly
while guess_of_user != computer_choice:
    user_input = input("Please enter your guess (a number between 1 and 10): ")

    # Check if the input is actually a number
    if user_input.isdigit():
        guess_of_user = int(user_input)
        number_of_guesses = number_of_guesses + 1  # Increase the guess count

        if guess_of_user < computer_choice:
            print("That guess was too low. Try again....")
        elif guess_of_user > computer_choice:
            print("That guess was too high. Try again.....")
        # No need for else here; if it's correct, loop will exit
    else:
        print("That doesn't look like a valid number. Please try again.")

# Step 5: When the guess is correct, congratulate the user
print("Well done! You guessed the number correctly.")
print("It only took you", number_of_guesses, "tries to get it right.")
