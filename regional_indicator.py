from string import ascii_lowercase
from sys import argv

converted = []

argv.pop(0)

args = " ".join(argv).lower()

for l in args:
	if l in list(ascii_lowercase): converted.append(":regional_indicator_{}: ".format(l))
	else: converted.append(" {} ".join(l))

print("".join(converted))