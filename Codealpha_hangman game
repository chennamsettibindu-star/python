import random

# Predefined words
words = ["python", "computer", "program", "coding", "hangman"]

# Select a random word
word = random.choice(words)

# Initialize variables
guessed_letters = []
attempts = 6
display_word = ["_"] * len(word)

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while attempts > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Result
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
