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
    "y": "ii",
    "ø": "'ur'",
    "ø̌": "'oh'",
    "ǔ": "'ao'",
    "ǎ": "'ow'",
    "ǒ": "'ou'"
}

consonants = {
    "b": "b",
    "d": "d",
    "dj": "j",
    "g": "g",
    "h": "h",
    "j": "jj'",
    "k": "k",
    "m": "m",
    "n": "n",
    "p": "p",
    "r": "rr",
    "s": "s",
    "sj": "sh",
    "t": "t",
    "tj": "tch",
    "v": "f",
    "w": "v",
    "z": "z"
}

formulas = [
    # wøt
    list("cvc"), 
    # wyjø
    list("cvcv"), 
    # iøg
    list("vvc"), 
    # ǎidø̌
    list("vvcv"), 
    # nyǎtø
    list("cvvcv"), 
    # ydusj
    list("vcvc")
]

def add_random_letter(letter_dict):
    random_num = random.random()
    
    random.seed(random_num)
    word_letter = random.choice(list(letter_dict.keys()))
    
    random.seed(random_num)
    pro_letter = random.choice(list(letter_dict.values()))
    
    word_list.append(word_letter)
    pro_word_list.append(pro_letter)

number_of_words = int(input("""How many words do you want to generate?\n>> """))

formula_yn = print("""Would you like to use a custom formula, or use the default ones?
(1) Custom Formula
(2) Default Formulas""")

loop = True
formula_list = []

while loop:
    formula_yn = input(">> ").strip().lower()
    
    if formula_yn == "1":
        formula_list.append(list(input("""[Formula Legend]
v = vowel
c = consonant

Example: cvc
What formula should the words follow?
>> """).strip().lower()))
        break
    
    elif formula_yn == "2":
        for i in range(number_of_words):
            word_list = []
            pro_word_list = []
            
            formula_list.append(random.choice(formulas))
        break
    
    else:
        print("That's not an option.")
        continue

# Seems ot only print 3 elements
for i in range(number_of_words):
    chosen_formula_list = random.choice(formula_list)
    word_list = []
    pro_word_list = []
    
    for letter in chosen_formula_list:
        if letter == "v": 
            add_random_letter(vowels)
        elif letter == "c": 
            add_random_letter(consonants)
        else:
            word_list.append(letter)
            pro_word_list.append(letter)
    
    print("Word {}: {}; Pronunciation: {}".format(i+1, "".join(word_list), "".join(pro_word_list)))
