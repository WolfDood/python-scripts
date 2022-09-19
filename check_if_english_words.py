# Requires PyEnchant spell checking library
# pip install pyenchant

import enchant

file_input = "./anglish-english-words2.txt"
file_output = "./anglish-english-words2-final.txt"

us_wordlist = []
gb_wordlist = []

with open(file_input, "r") as f:
    us_d = enchant.Dict("en_US")
    gb_d = enchant.Dict("en_GB")
    # word_num = len(f.readlines())
    for i, word in enumerate(f):
        # print(f"Checking word {i+1}/{word_num}")
        print(f"Checking word {i+1}")
        word = word.strip()
        # input(f"Word is '{word}'.")
        if us_d.check(word):
            # print("Added to US WL")
            us_wordlist.append(word)
        if gb_d.check(word):
            # print("Added to GB WL")
            gb_wordlist.append(word)
    print("Finished checking!")

print("Merging word lists...")
word_list = list(set(us_wordlist + gb_wordlist))
word_list = sorted(word_list)

with open(file_output, "w") as f:
    print("Writing to file...")
    for word in word_list:
        f.write(f"{word}\n")
    print("Done!")
