import random
import art_stages_logo as art

print(art.logo,"\n")

while True:
    try:
        lang = int(input("1 for English words or 2 for Swedish:"))
        if lang in [1, 2]:
            break
        else:
            print("Invalid input. Please enter 1 or 2.\n")
    except ValueError:
        print("Invalid input. Please enter a number.")

#import word list in users choice of language

if lang == 1:
    import word_list_eng as word_list
else:
    import word_list_swe as word_list

challenge_level = int(input("Välj längd på ordet. 7, 8, 9, 10 eller 11:"))

display = []

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
        print("\nFörsök igen.\n")
        continue

#give the lenght of the word
word_lenght = len(hidden_word)

for _ in range(word_lenght):
    display += "▓"

print(" ".join(display))

guess = input(f"Guess character in the {challenge_level} letter word").lower()
life = len(hidden_word)

for position in range(word_lenght):
    letter = hidden_word[position]
    if letter == guess:
        display[position] = letter
        print("Right!")
        print(" ".join(display))

print(" ".join(display))