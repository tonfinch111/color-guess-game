import random

def main():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    correct_color = random.choice(colors)
    attempts = 0

    print("Welcome to the Color Guessing Game!")
    print("Try to guess the correct color from this list:")
    print(", ".join(colors))

    while True:
        guess = input("Enter your guess: ").strip().lower()
        attempts += 1

        if guess == correct_color:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
        elif guess in colors:
            print("Incorrect. Try again!")
        else:
            print("Invalid color. Try one of:", ", ".join(colors))

if __name__ == "__main__":
    main()

