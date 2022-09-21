file_name = "./wordlist-b-left.txt"

words = {}
duplicates = []

with open(file_name, "r") as f:
    print("Finding duplicates...")
    for i, line in enumerate(f):
        line = line.strip()
        line_number = i + 1

        if line in words.keys():
            # print("Duplicate found.")
            words[line].append(line_number)
            duplicates.append(line)
        else:
            words.update({line: [line_number]})

print("File searched and closed.")

print("Getting rid of duplicates in duplicate list...")
duplicates = list(set(duplicates))

print("Printing out results:\n")

for d in duplicates:
    print(f" word '{d}' has duplicates at lines: {words[d]}")
