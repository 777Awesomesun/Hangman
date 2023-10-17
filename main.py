import time
import random
import art_stages_logo as art

display = []

end_of_game = False 

def game_over():
    print("You loose!")
    dramatisk_paus()
    print("Bättre lycka nästa gång!")
    exit() 

def dramatisk_paus():
    time.sleep(0.5)

def visual_hangman():
    if life == 11:
        print(art.stages[11])
    elif life == 10:
        print(art.stages[10])
    elif life == 9:
        print(art.stages[9])
    elif life == 8:
        print(art.stages[8])
    elif life == 7:
        print(art.stages[7])
    elif life == 6:
        print(art.stages[6])
    elif life == 5:
        print(art.stages[5])
    elif life == 4:
        print(art.stages[4])
    elif life == 3:
        print(art.stages[3])
    elif life == 2:
        print(art.stages[2])
    elif life == 1:
        print(art.stages[1])
    elif life == 0:
        print(art.stages[0])

print(art.logo,"\n")

#When user gets <0 life he come here to the game over function

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

#import word list in users choice of language

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
print(" ".join(display))

dramatisk_paus()
print(hidden_word, "\n")


print(life)

#The main functio.
#The user guesses a letter and we itirate through all the letters from the hidden word in the
#word and sees if it is a match.

while not end_of_game:
    dramatisk_paus()
    guess = input(f"Guess letter in the {challenge_level} letter word\n").lower()

    for position in range(word_lenght):

        letter = hidden_word[position]

        if letter == guess:
            dramatisk_paus()
            display[position] = letter
            print("Right!\n")
            visual_hangman()
            dramatisk_paus()
            print(" ".join(display))
            dramatisk_paus()
            print(life)

    if guess not in hidden_word:
        life -= 1
        dramatisk_paus()
        print("Wrong!")
        visual_hangman()
        print(" ".join(display))
        dramatisk_paus()
        print(life)
    
    if "▓" not in display:
        dramatisk_paus()
        print("You win!")
        end_of_game = True
    
    elif life <= 0:
        dramatisk_paus()
        print(art.stages[0])
        for u in range(20):
            print(art.stages[u])
        break