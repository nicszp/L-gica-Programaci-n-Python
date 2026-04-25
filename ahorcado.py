# create your word list
# randomly choose a word from the list you have created
# ask the user to guess a letter
# bonus make the program take the input from the user and make it lowercase
# check if the letter is in the word

# Loop through each of the letters in the chosen word
# if the letter is in the word replace the "_" with the letter
# it should look like this "_","a","c","_","_","r"

import random

word = ["carlos", "maria", "jose"]

secret_word = random.choice(word)

display_word = ["_"] * len(secret_word)

print(f"Adivina la palabra: {display_word}")

while "_" in display_word:
    guess = input("Adivinan una letra para ver si esta en la palabra: ")

    for i in range(len(secret_word)):
        if secret_word [i] == guess:
            display_word [i] = guess

    print(display_word)

print("You Win")

