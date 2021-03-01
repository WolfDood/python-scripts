# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:23:58 2021

@author: https://github.com/kaubu
"""

import random

vowels = {
    "a": "ae",
    "e": "e",
    "i": "i",
    "o": "o",
    "u": "a",
    "y": "ii"
}

consonants = {
    "b": "b",
    "d": "d",
    "g": "g",
    "h": "h",
    "j": "j'",
    "k": "k",
    "m": "m",
    "n": "n",
    "s": "s",
    "sj": "sh",
    "t": "t",
    "tj": "ch",
    "v": "f",
    "w": "v",
}

number_of_words = int(input("How many words do you want to generate? "))

formula_list = list(input("""[Formula Legend]
v = vowel
c = consonant

Example: cvc
What formula should the words follow? """).strip().lower())

def add_random_letter(letter_dict):
    random_num = random.random()
    
    random.seed(random_num)
    word_letter = random.choice(list(letter_dict.keys()))
    
    random.seed(random_num)
    pro_letter = random.choice(list(letter_dict.values()))
    
    word_list.append(word_letter)
    pro_word_list.append(pro_letter)

for i in range(number_of_words):
    word_list = []
    pro_word_list = []
    
    for letter in formula_list:
        if letter == "v": 
            add_random_letter(vowels)
        elif letter == "c": 
            add_random_letter(consonants)
        else:
            word_list.append(letter)
            pro_word_list.append(letter)
    
    print("Word {}: {}; Pronunciation: {}".format(i, "".join(word_list), "".join(pro_word_list)))