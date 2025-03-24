import random

def play_game():
    print("Welcome the the number guessing game")
    print("Choose a difficulty level")
    print("1. Easy(10 attempts)")
    print("2.Medium(7 attempts)")
    print("3.Hard(3 attempts)")

    while True:
        try:
            choice = int(input("Enter your choice 1/2/3: "))
            if choice == 1:
                max_attempts = 10
                break
            elif choice == 2:
                max_attempts = 7
                break
            elif choice == 3:
                max_attempts = 3
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input")

    secret_number = random.randint(1, 100)
    print(f"A number between 1 and 100.You have {max_attempts} attempts left!")

    for attempt in range(1, max_attempts + 1):
        while True:
            try:
                guess = int(input(f" Current attempt {attempt}/{max_attempts}: Enter your guess: "))
                break
            except ValueError:
                print("Invalid input")

        if guess == secret_number:
            print(f"Congrats! You guessed {secret_number} correctly!")

        else:
            print(f"Sorry! You guessed incorrectly!")

while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thank you for playing")
        break
