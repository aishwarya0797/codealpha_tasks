import random


def choose_word():
    """Return a random word from a predefined list of 5 words."""
    words = ["apple", "tiger", "house", "plant", "robot"]
    return random.choice(words)


def get_display_word(secret_word, guessed_letters):
    """
    Return the word display with underscores for unguessed letters.
    Example: '_ p p _ e'
    """
    display = []
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)


def get_valid_guess(guessed_letters):
    """Prompt user until a valid single alphabet letter is entered."""
    while True:
        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1:
            print("Invalid input. Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Invalid input. Please enter an alphabet letter (a-z).")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        else:
            return guess


def play_hangman():
    """Run one full game of Hangman."""
    secret_word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n=== Welcome to Hangman ===")
    print("Guess the word one letter at a time.")
    print(f"You can make only {max_wrong_guesses} wrong guesses.\n")

    while wrong_guesses < max_wrong_guesses:
        current_display = get_display_word(secret_word, guessed_letters)
        print("Word:", current_display)
        print("Guessed letters:", " ".join(guessed_letters) if guessed_letters else "None")
        print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

        # Win check
        if "_" not in current_display:
            print("\nCongratulations! You guessed the word correctly:", secret_word)
            return

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

    # If loop ends, user lost
    print("Game Over! You used all 6 wrong guesses.")
    print("The correct word was:", secret_word)


if __name__ == "__main__":
    play_hangman()