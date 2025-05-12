import random

# Word list to choose from
word_list = ["python", "hangman", "challenge", "programming", "developer", "function", "variable"]

# Select a random word from the list
word = random.choice(word_list)
word_letters = set(word)  # Unique letters in the word
guessed_letters = set()   # Letters the player has guessed
wrong_guesses = set()     # Incorrect guesses

# Set the number of allowed incorrect attempts
max_attempts = 6

print("Welcome to Hangman!")
print("_ " * len(word))

while len(word_letters) > 0 and len(wrong_guesses) < max_attempts:
    print("\nGuessed so far:", " ".join(guessed_letters))
    print("Wrong guesses:", " ".join(wrong_guesses))
    print(f"Remaining attempts: {max_attempts - len(wrong_guesses)}")

    # Display current progress
    word_display = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word: ", " ".join(word_display))

    # Player input
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters or guess in wrong_guesses:
        print("You already guessed that letter.")
        continue

    if guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("Correct!")
    else:
        wrong_guesses.add(guess)
        print("Wrong!")

# Game over logic
if len(wrong_guesses) >= max_attempts:
    print("\nYou lost! The word was:", word)
else:
    print("\nCongratulations! You guessed the word:", word)
