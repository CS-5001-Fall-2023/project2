import random # library required to randomly choose a secret word

def get_secret_word() -> str:
	"""
	Returns a randomly generated secret word.
	Uses the list of words in the public domain retreived from:
	https://www-cs-faculty.stanford.edu/~knuth/sgb.html
	Requires a text file called words.txt.	
	"""
	with open('words.txt') as f:
		words = f.read().splitlines() 		
		word = random.choice(words)
	return word

def main():
	pass

if __name__ == '__main__':
    main()