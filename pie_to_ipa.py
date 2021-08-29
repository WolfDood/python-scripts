primary_stress = "ˈ" # Can only be at the start of a word
secondary_stress = "ˌ"

pie_to_ipa = {
	# Consonants
	"b": "b", 
	"d" :"d", 
	"dh": "ð", 
	"f" :"f", 
	"g" :"g", 
	"h" :"h", 
	"j" :"j", 
	"k" :"k", 
	"l" :"l", 
	"m" :"m", 
	"n" :"n", 
	"ng": "ŋ", 
	"p" :"p", 
	"r" :"r", 
	"s" :"s", 
	"c": "ʃ", 
	"t" :"t", 
	"tc": "tʃ", 
	"th": "θ", 
	"v" :"v", 
	"w" :"w", 
	"z" :"z", 
	"zh": "ʒ",
	# Diphthongs
	"ai": "aɪ",
	"ei": "eɪ",
	"oi": "ɔɪ",
	"au": "aʊ",
	# Vowels
	"a": "a",
	"o": "ɒ",
	"æ": "æ",
	"ae": "æ",
	"e": "e",
	"y": "ɪ", 
	"i": "i",
	"u": "u",
	# Stressed Vowels
	"á": "ˌaː",
	"ó": "ˌɒː",
	"ǽ": "ˌæː",
	"é": "ˌeː",
	"ý": "ˌɪː", 
	"í": "ˌiː",
	"ú": "ˌuː",
}

while True:
	to_translate = input("> ")

	for pie, ipa in pie_to_ipa.items():
		to_translate = to_translate.replace(pie.lower(), ipa)
	
	# Find all lower stresses and move them back one
	for i, char in enumerate(to_translate):
		if char == secondary_stress:
			t = list(to_translate)
			t[i], t[i-1] = t[i-1], t[i] # Swaps characters at index
			to_translate = "".join(t)

	# If lower stress is at start of a word (i.e., there's a space behind it, change it to upper stress)
	for i, char in enumerate(to_translate):
		if char == secondary_stress:
			if to_translate[i-1] == " " or i == 0:
				t = list(to_translate)
				t[i] = primary_stress
				to_translate = "".join(t)
	
	print(to_translate)
