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

for i in range(number_of_words):
    word_list = []
    pro_word_list = []
    for letter in formula_list:
        if letter == "v":
            random_num = random.random()
            random.seed(random_num)
            word_list.append(random.choice(list(vowels.keys())))
            random.seed(random_num)
            pro_word_list.append(random.choice(list(vowels.values())))
        elif letter == "c":
            random_num = random.random()
            random.seed(random_num)
            word_list.append(random.choice(list(consonants.keys())))
            random.seed(random_num)
            pro_word_list.append(random.choice(list(consonants.values())))
        else:
            random_num = random.random()
            random.seed(random_num)
            word_list.append(list(letter.keys()))
            random.seed(random_num)
            pro_word_list.append(list(letter.values()))
    
    print("Word {}: {}; Pronunciation: {}".format(i, "".join(word_list), "".join(pro_word_list)))