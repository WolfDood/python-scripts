import itertools

letters = [
    "p",
    "b",
    "t", 
    "d",
    "k", 
    "g",
    "s", 
    "z",
    "c",
    "cz",
    "f",
    "v",
    "th",
    "dh",
    "m",
    "n",
    "hh",
    "r",
    "j",
    "l",
    "w",
]

for i, c in enumerate(list(itertools.combinations(letters, 2))):
    print(f"{c[0]}{c[1]}")
