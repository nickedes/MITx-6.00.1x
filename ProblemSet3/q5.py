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
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    a='abcdefghijklmnopqrstuvwxyz'
    b=''
    for i in a:
    	if i not in lettersGuessed:
    		b+=i
    return b

def hangman(secretWord):
	'''
	secretWord: string, the secret word to guess.

	Starts up an interactive game of Hangman.

	* At the start of the game, let the user know how many 
	letters the secretWord contains.

	* Ask the user to supply one guess (i.e. letter) per round.

	* The user should receive feedback immediately after each guess 
	about whether their guess appears in the computers word.

	* After each round, you should also display to the user the 
	partially guessed word so far, as well as letters that the 
	user has not yet guessed.

	Follows the other limitations detailed in the problem write-up.
	'''
	print "welcome to the game, Hangman!"
	f=0
	print "I am thinking of a word that is "+str(len(secretWord))+" letters long."
	lettersGuessed = ''
	i=0
	while i<8:
		print "-------------"
		print "You have "+str(8-i) +" guesses left."
		print "Available letters: "+str(getAvailableLetters(lettersGuessed))
		guess=raw_input("Please guess a letter: ")
		guess=guess.lower()
		if guess in lettersGuessed:
			print "Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed))
		else:
			lettersGuessed+=guess
			if guess in secretWord:
				 print "Good guess: "+str(getGuessedWord(secretWord, lettersGuessed))	
				 if secretWord == getGuessedWord(secretWord, lettersGuessed):
				 	print "-------------"
				 	print "congratulations, you won!"
				 	f=1
				 	break
			else :
				i=i+1
				print "Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed))
	if f==0 and i==8:
		print "-------------\nSorry, you ran out of guesses. The word was "+str(secretWord)+". "						
hangman('apple')		
