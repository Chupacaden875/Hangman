import random

# Declare max_attempts as a global variable
max_attempts = 6

def choose_word():
    #Choose a random word from a list of fruits.
    fruits = ["apple", "banana", "orange", "grape", "strawberry", "kiwi", "watermelon", "pineapple"]
    return random.choice(fruits)

def display_word(word, guessed_letters):
    #Display the current state of the word with guessed letters.
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def display_hangman(attempts_left):
    #Display the hangman graphics based on the number of attempts left.
    hangman_graphics = [
        """
        ------
        |    |
        |
        |
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |    |
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |   /|
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |
        -
        """
        ,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        -
        """
    ]
    return hangman_graphics[max_attempts - attempts_left]

def hangman():
    """Main function for playing the Hangman game."""
    global max_attempts  # Declare max_attempts as a global variable
    guessed_letters = []
    word_to_guess = choose_word()
    attempts_left = max_attempts

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts_left > 0:
        guess = input("Guess a letter: ").lower()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the guessed letter is already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is incorrect
        if guess not in word_to_guess:
            attempts_left -= 1
            print(f"Incorrect! Attempts left: {attempts_left}")
            print(display_hangman(attempts_left))
        else:
            print("Correct!")

        # Display the current state of the word
        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        # Check if the word is completely guessed
        if "_" not in current_display:
            print("Congratulations! You guessed the word.")
            break

    # Display the result if no attempts left
    if attempts_left == 0:
        print(f"Sorry, you ran out of attempts. The correct word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
