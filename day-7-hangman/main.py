from libraries import random_word_selector

word = random_word_selector()

user_input = input("Guess your alphabet: ")

def checking_guess(user_input,word):
    if user_input.lower() in word:
        print("right")
    else:
        print("wrong")

for i in range(0,len(word)):
    checking_guess(user_input,word)



