# Simple number guessing program using a while loop

secret_number = 7
user_guess = 0

print("Welcome. Try to guess the secret number between 1 and 10.")

# The loop keeps running until the user enters the correct number
while user_guess != secret_number:
    user_guess = int(input("Enter your guess: "))
    
    if user_guess < secret_number:
        print("Too low. Try again.")
    elif user_guess > secret_number:
        print("Too high. Try again.")

print("Correct. You guessed the secret number.")
