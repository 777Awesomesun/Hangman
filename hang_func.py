hidden_word = "bamselina"
word_lenght = len(hidden_word)

challenge_level = 7

# life = len(hidden_word)

guess = "a"

# display = ["▓", "▓", "▓", "▓", "▓", "▓", "▓", "▓", "▓", "▓", "▓"]

# while True:
#     user_guess = input(f"Guess character in the {challenge_level} letter word").lower()

#     for i in hidden_word:
#         if i == user_guess:
#             print("Right!")
#         elif user_guess == i:
#             hidden_word[i] = i
#         else:
#             print("Wrong")
#     break

# for i in hidden_word:
#     if i == user_guess:
#         print("Right!")
#     elif user_guess == i:
#         hidden_word[i] = i
#     else:
#         print("Wrong")

# display = []

# for _ in range(word_lenght):
#     display += "_"

# for position in range(word_lenght):
#     letter = hidden_word[position]
#     if letter == guess:
#         display[position] = guess



print(display)

# blanks_itirations = len(hidden_word)

# print(hidden_word)
# for i in range(blanks_itirations):
#     first = display[i]
#     print(first, end=" ")