# Description of problem found at http://codeforces.com/problemset/problem/131/A


def main():
	in_string = input()
	
	# assume it is caps lock
	follows_rules = True
		
	for character in in_string[1:]:
		# If the character is lowercase,
		# this does not follow the rules
		# of our caps lock determination.
		if character != character.upper():
			follows_rules = False
			break
		
	if follows_rules:
		for character in in_string:
			# Invert the casing of the character
			if character != character.upper():
				print(character.upper(), end="")
			else:
				print(character.lower(), end="")
	else:
		print(in_string)
	

if __name__ == "__main__":
	main()