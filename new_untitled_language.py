ipa = {
	# Special
	" ": " ",
	"'": "", # Placeholder character, has no sound
	"`": "", # Alt placeholder character
	"‘": "", # Second verse, same as the first
	"’": "",
	# Consonants
	"b": "b",
	"d": "d",
	"t": "t",
	"g": "g",
	"k": "k",
	"j": "ʒ", # Vi -si- on
	"s": "s",
	"m": "m",
	"n": "n",
	"f": "f",
	"v": "v",
	"r": "r", # r is rolled r, upside down r is -r- ed
	"z": "z",
	"l": "l",
	"p": "p",
	"h": "h",
	# Vowels
	"a": "ɑ",
	"e": "ɛ", # b -e- d
	"o": "o",
	"i": "ɪ", # b -i- t
	"y": "i", # ee
	"u": "u",
}

if __name__ == "__main__":
	print("New Untitled Language Translator v1.0.1")
	while True:
		sentence = input("Please enter a sentence to translate from New Untitled Language to IPA. Type \":exit\" to exit.\n>> ")
		if sentence == ":exit" or sentence == ":e": break

		translated = []
		for char in list(sentence):
			if char not in ipa and char.lower() not in ipa:
				print(f"Invalid character: \"{char}\"")
				continue
			translated.append(ipa[char.lower()])
		
		result = "".join(translated)
		print(f"Result:\n{result}")
