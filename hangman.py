# Welcome and Instructions
print("Welcome to Hangman, please ask a person to input a word!")
word = input()
word = word.lower()
guesses = 5
# User Input and Exit
while guesses > 0:
    # Options and HAL
    print("Please guess a letter")
    letter = input()

    letter = letter.lower()
    guesses = guesses - 1

    word = list(word)

    if letter in word:
        print('you got it')

        print(letter)
        print("resides at index ")
        print(word.index(letter))
    else:
        print("sorry please guess again!")

print('Game over, want to play again?')
