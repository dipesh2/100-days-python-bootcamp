import random

def random_word_selector():
    list_of_words = ["apple","car","house","mouse"]
    word = random.choice(list_of_words)
    return word


def blanks_creation(word):
    no_of_lives = len(word)
    return no_of_lives