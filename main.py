import time
import random
import art_stages_logo as art

display = []

gissade_ord = []

end_of_game = False 

#When user gets <0 life he come here to the "game over" function

def display_word():
    print(" ".join(display))

def game_over():
    print("You loose!")
    dramatisk_paus()
    print("Bättre lycka nästa gång!")
    exit() 

def dramatisk_paus():
    time.sleep(0.5)

def visual_hangman():
    print(art.stages[life])

print(art.logo,"\n")

while True:
    try:
        lang = int(input("1 for English words or 2 for Swedish:"))
        if lang in [1, 2]:
            break
        else:
            dramatisk_paus()
            print("Invalid input. Please enter 1 or 2.\n")
    except ValueError:
        dramatisk_paus()
        print("Invalid input. Please enter a number.")
'''
#import word list in users choice of language
'''

if lang == 1:
    import word_list_eng as word_list
else:
    import word_list_swe as word_list

challenge_level = int(input("Välj längd på ordet. 7, 8, 9, 10 eller 11:"))

#generate the hidden word

while True:
    if challenge_level == 7:
        hidden_word = random.choice(word_list.seven_letter_words)
        break
    elif challenge_level == 8:
        hidden_word = random.choice(word_list.eight_letter_words)
        break
    elif challenge_level == 9:
        hidden_word = random.choice(word_list.nine_letter_words)
        break
    elif challenge_level == 10:
        hidden_word = random.choice(word_list.ten_letter_words)
        break
    elif challenge_level == 11:
        hidden_word = random.choice(word_list.eleven_letter_words)
        break
    else:
        dramatisk_paus()
        print("\nFörsök igen.\n")
        continue

if challenge_level == 7:
    life = 7
elif challenge_level == 8:
    life = 8
elif challenge_level == 9:
    life = 9
elif challenge_level == 10:
    life = 10
elif challenge_level == 11:
    life = 11

visual_hangman()

#give the lenght of the word
word_lenght = len(hidden_word)

for _ in range(word_lenght):
    display += "▓"

dramatisk_paus()
display_word()

''' 
The main function. The user guesses a letter and we itirate through all the letters 
from the hidden word in the and sees if it is a match.
'''

while not end_of_game:
    dramatisk_paus()
    guess = input(f"Guess letter in the {challenge_level} letter word, you have {life} life left.\n").lower()

    for position in range(word_lenght):

        letter = hidden_word[position]

        if letter == guess:
            dramatisk_paus()
            display[position] = letter
            print("Right!\n")
            visual_hangman()
            dramatisk_paus()
            display_word()
            dramatisk_paus()
            
    if guess not in hidden_word and guess not in gissade_ord:
        life -= 1
        dramatisk_paus()
        print("That letter is not in the word.")
        gissade_ord.append(guess)
        dramatisk_paus()
        visual_hangman()
        display_word()
    elif guess not in hidden_word and guess in gissade_ord:
        print()
        gissade_ord.append(guess)
        print("You already guessed that!\n")
    

    
    if "▓" not in display:
        dramatisk_paus()
        print(art.win_logo)
        print("You win!")
        end_of_game = True
    
    elif life <= 0:
        dramatisk_paus()
        print(art.gameover_logo)
        samman_gissade_ord = ", ".join(gissade_ord)
        print(f"You guessed {samman_gissade_ord}. and the word was {hidden_word}")
        break