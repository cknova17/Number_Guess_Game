import random

print("Welcome to number guessing game!")
while True:
    name = input("What is your name? ")
    print("Hi", name, "-let's play!")
    # computer secretly picks a number between 1 to 10
    secret_number = random.randint(1, 10)
    print("Okay,", name + ", I'm thinking of a number between 1 and 10")
    # print("(psst...the secret is " , secret_number, ")")
    # lets make the player guess, so start with a dummy value)
    guess = 0
    attempts = 0
    max_attempts = 5
    # guessing loop begins
    while attempts < max_attempts:
        guess = int(input("Take a guess:"))
        attempts += 1
        print("Attempts", attempts , "of ", max_attempts)
        if guess < secret_number:
            print("Your guess is too low.Try again")
        elif guess > secret_number:
            print("Your guess is too high.Try again")
        else:
            print("Correct!", name, "You guessed it right in", attempts, "tries!")
            break
    # After the guessing loops ends with all failed attempts
    if guess != secret_number:
        print(":-) Game Over,", name + "!")
        print("The secret number was", secret_number)
    # Ask if they want to play again
    play_again = input("Do you want to play again? (Y/N):").lower()
    if play_again != "y":
        print("Thank you for playing," + name + "Bye!")
        break
