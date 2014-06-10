
def isWordGuessed(secretWord, lettersGuessed):
	'''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
	'''
	letters=[secretWord[0]]
	for i in range(0,len(secretWord)):
		if secretWord[i] not in letters:
			letters+=secretWord[i]
	for i in range(0,len(letters)):
		if letters[i] not in lettersGuessed:
			return False
	return True
print isWordGuessed('banana', ['z', 'x', 'q', 'b', 'a', 'n', 'a', 'n', 'a'])	
			
