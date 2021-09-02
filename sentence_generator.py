import random
articles = ("A", "The")
nouns = ("BOYS", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = (r"WITH", "BY")

def sentence():
	return nounPhrase() + " " + verbPhrase()

def nounPhrase():
	return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
	return random.choice(verbs) + " " + nounPhrase() +" "+ perpositionalPhrase() 

def perpositionalPhrase():
	return random.choice(prepositions) + " " + nounPhrase()

if __name__ == '__main__':
	number = int(input("Enter the Number of sentences:"))
	for i in range(number):
		print(sentence())