import random
words_list = ["PYTHON", "CODE", "ALPHA", "GITHUB", "ENGINEER"]
secret_word = random.choice(words_list)
guessed_letters = []
wrong_guesses_left = 6
print("=== WELCOME TO CODEALPHA HANGMAN GAME ===")
print(f"Total wrong attempts allowed: {wrong_guesses_left}")
print("-----------------------------------------")
while wrong_guesses_left > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"\nWord: {display_word} | Attempts left: {wrong_guesses_left}")
    print(f"Guessed letters so far: {guessed_letters}")

    if "_" not in display_word:
        print(f"\n🎉 CONGRATULATIONS! Word was: {secret_word}")
        break

    user_guess = input("Enter a letter: ").upper().strip()

    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Invalid input! Enter a single alphabetical letter.")
        continue

    if user_guess in guessed_letters:
        print("You already guessed that letter! Try again.")
        continue

    guessed_letters.append(user_guess)

    if user_guess in secret_word:
        print(f"Good job! '{user_guess}' is in the word.")
    else:
        print(f"Wrong guess! '{user_guess}' is not in the word.")
        wrong_guesses_left -= 1

if wrong_guesses_left == 0:
    print(f"\n💥 GAME OVER! The correct word was: {secret_word}")