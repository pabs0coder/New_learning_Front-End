# Write your code here
import random

tries = 8
my_list = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N\n')
word = random.choice(my_list)
hidden_word = list('-' * len(word))
used_letters = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
other_used= []

ask = input("Type 'play' to play the game, 'exit' to quit:")
print (ask)
if ask == "play":
    while tries > 0:
        print('\n')
        print(''.join(hidden_word))
        guess = input('Input a letter: ')


        if len(guess) >1:
            print("You should input a single letter")
            continue
        elif guess not in alphabet:
            print("Please enter a lowercase English letter")
            continue
        elif guess in other_used:
            print("You've already guessed this letter")
            other_used.append(guess)
        elif guess not in word:
            print("That letter doesn't appear in the word")
            other_used.append(guess)
            tries -= 1
            if tries == 0:
                print("That letter doesn't appear in the word")
                print('You lost!')
        elif guess not in other_used:
            print("That letter doesn't appear in the word")
            tries -= 1
            other_used.append(guess)
            if tries == 0:
                print('You lost!')
                break
            continue
        elif guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
else:
    exit




