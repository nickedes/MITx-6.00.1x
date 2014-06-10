Q1 Computes and returns the amount of radiation exposed to between the start and stop times. Calls the function f (defined for you in the grading script) to obtain the value of the function at any point.
 start: integer, the time at which exposure begins
 stop: integer, the time at which exposure ends
 step: float, the width of each rectangle. You can assume that
 the step size will always partition the space evenly.
 returns: float, the amount of radiation exposed to between start and stop times.
 
 Q2 Implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.
 
 Q3 Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!
 
 Q4 Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
 
 Q5 Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.
