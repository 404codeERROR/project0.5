import random

words = ["apple", "table", "chair", "money", "robot"]
word = random.choice(words)
guessed = []
tries = 6

print("Welcome to Hangman!")
print("_ " * len(word))

while tries > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct!")
    else:
        print("Wrong!")
        tries -= 1

    display = [letter if letter in guessed else "_" for letter in word]
    print(" ".join(display))

    if "_" not in display:
        print("You win!")
        break
else:
    print("You lose! The word was:", word)