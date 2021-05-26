import random
from words import words
import string


def get_vallid_word(wordss):
    word = random.choice(wordss)
    while '_' in word or ' '  in word:
        word = random.choice(wordss)
    return word.upper()

def hangman():
    word = get_vallid_word(words)
    # word = random.choice(words).upper()
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letter)>0:
        words_list = [letter if letter in used_letters else '_' for letter in word]
        print(f"Letters You already ued are: " , ', '.join(used_letters))
        print("letters are: ", " ".join(words_list))
        user_letter = str(input("\nEnter the Letter: \n")).upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

        elif user_letter in used_letters:
            print("You already used that word! ")     

        else:
            print("Not something valid!")    
    print(f"Yes the word is: {word}")       
hangman()