import random

def word_guessing_game():
    word_list = ["I Like You Fiza"]
    word = random.choice(word_list)
    word_length = len(word)
    print("The word has", word_length, "letters.")
    word_guessed = ["_"] * word_length
    print(" ".join(word_guessed))
    attempts = 0
    while "_" in word_guessed:
        user_input = input("Enter a letter: ")
        if user_input in word:
            for i in range(word_length):
                if word[i] == user_input:
                    word_guessed[i] = user_input
            print(" ".join(word_guessed))
        else:
            attempts += 1
            print("Incorrect! Attempts left: ", 5 - attempts)
        if attempts >= 5:
            print("You Lost! The word was: ", word)
            break
    print("You Won! The word was: ", word)

word_guessing_game()
