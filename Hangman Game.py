import random

# List of predefined words
words = ["python", "apple", "chair", "tiger", "planet"]

# Select a random word
word = random.choice(words)

# Create empty display
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("Welcome to Hangman Game!")

# Game loop
while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", guessed_letters)
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct Guess!")

        # Reveal the letter in the word
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong Guess!")
        attempts -= 1

# Final result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)