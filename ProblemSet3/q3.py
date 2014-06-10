
def  getGuessedWord(secretWord, lettersGuessed):
	'''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
	'''
	a=''
	letters=[secretWord[0]]
	# for i in range(0,len(secretWord)):
	for i in range(0,len(secretWord)):
		if secretWord[i] in lettersGuessed:
			a+=secretWord[i]
		else :
			a+='_'	
	return a
print  getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])	
			
