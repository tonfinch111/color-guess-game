import random

def get_random_color():
    colors = ["red", "blue", "green", "yellow", "orange", "purple"]
    return random.choice(colors)

def play_game():
    print("Welcome to the Color Guessing Game!")
    secret_color = get_random_color()
    attempts = 3

    while attempts > 0:
        guess = input(f"Guess the color ({attempts} attempts left): ").lower()
        if guess == secret_color:
            print("Congratulations! You guessed it right!")
            break
        else:
            print("Wrong guess. Try again.")
            attempts -= 1

    if attempts == 0:
        print(f"Game over! The correct color was '{secret_color}'.")

if __name__ == "__main__":
    play_game()

