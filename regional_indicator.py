from string import ascii_lowercase
from sys import argv

converted_message = []

argv.pop(0)

message = " ".join(argv).lower()

for letter in message:
	if letter in list(ascii_lowercase): converted_message.append(f":regional_indicator_{letter}: ")
	else: converted_message.append(" {} ".join(letter))

print("".join(converted_message))
