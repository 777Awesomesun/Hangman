import random
import art_stages_logo as art

print(art.logo,"\n")
lang = int(input("1 För Engelska ord eller 2 för Svenska:"))

#import word list in users choice of language

if lang == 1:
    import word_list_eng as word_list
else:
    import word_list_swe as word_list

challenge_level = int(input("Välj längd på ordet. 7, 8, 9, 10 eller 11:"))

bbblanks = word_list.blanks

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

blanks_itirations = len(hidden_word)
print("\n")
for i in range(blanks_itirations):
    first = bbblanks[i]
    print(first, end=" ")
