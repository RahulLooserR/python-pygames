# file name : hangman.py
# description : hangman game, in which player 1 gives a word with missing 
#               letters. player 2 has to guess the letters. if player 2 fails, 
#               each time hangman picture will grow. and when hangman picture 
#               is completed, player 2 loose.

import random

def display ():
	print ('''Hangman is a game for two people in which one player thinks of a 
word and then draws a blank line on the page for each letter in the word. 
The second player then tries to guess letters that might be in the word.
If the second player guesses the letter correctly, the first player writes
the letter in the proper blank. But if the second player guesses 
incorrectly, the first player draws a single body part of a hanging man.
The second player has to guess all the letters in the word before the 
hanging man is completely drawn to win the game.''')

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
O   |
    |
    |
   ===''', '''
+---+
O   |
|   |
    |
   ===''', '''
 +---+
 O   |
/|   |
     |
    ===''','''
 +---+
 O   |
/|\  |
     |
    ===''','''
 +---+
 O   |
/|\  |
     |
    ===''','''
 +---+
 O   |
/|\  |
/    |
    ===''','''
 +---+
 O   |
/|\  |
/ \  |
    ===''']

print ('Let\'s start the game')

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad turkey turtle weasel whale wolf wombat zebra'.split()

alphabets = 'abcdefghijklmnopqrstuvwxyz'

# function definiton for getting random word from the list
def getRandomWord (wordList):
	index = random.randint (0, len(wordList) - 1)
	return wordList[index]

# function definition for displaying the hangman pics and missed letters and 
# correct letters
def displayBoard (mLetters, cLetters, secretWord):
	# mLetters : missedletters
	# cletters : correct letters
	
	print (HANGMAN_PICS[len(mLetters)])
	print ()
	
	print ('Letter Missed :', end = ' ')
	
	for letters in mLetters:
		print (letters, end = ' ')
	
	print ()
	
	blanks = '-' * len (secretWord)

# placing correct letters at their right places
	for i in range (len (secretWord)):
		if secretWord[i] in cLetters :
			blanks = blanks[:i]+secretWord[i]+blanks[(i+1):]

# display correct letters and the missing in '-'.
	print ('correct letters: '+blanks)

	for letter in mLetters :
		print (letter, end = ' ')
	
	print ()

# function definition for getting input from user
def getguess (guessed):
	# input validation
	while True:
		print ('Guess a letter : ', end = '')
		guess = input ()
		guess = guess.lower()

		if len (guess) != 1:
			print ()
			print ('please enter a letter only')
		
		elif guess in guessed:
			print ('you have already guessed the letter, try another')
		
		elif guess not in alphabets:
			print ('please enter letter only')
		else:
			return guess

# funtion to prompt the user to ask again
def playAgain ():
	print ('Do you want to play again [y/n] : ', end = '')
	
	while True:
		result = input()
		if result == 'y':
			return 1
		elif result == 'n':
			return 0
		else :
			print ('Enter only \'y\' or \'n\' : ', end = '')

 
print ('HANGMAN')
print ('=======')
mLetters = ''
cLetters = ''
secretWord = getRandomWord (words)
gameOver = False

display ()
while True:
	
	displayBoard (mLetters, cLetters, secretWord)

	guess = getguess (mLetters + cLetters)
	
	if guess in secretWord:
		cLetters = cLetters + guess
		
		foundAllLetters = True
		for i in range (len (secretWord)):
			if secretWord[i] not in cLetters:
				foundAllLetters = False
				break
		
		if foundAllLetters:
			print ('you win \n the secret word is ' +'\'' + secretWord + '\'')
			gameOver = True
	else:
		mLetters = mLetters + guess
	
		displayBoard (mLetters, cLetters, secretWord)

		if len (mLetters) == len (HANGMAN_PICS) - 1:
			print ('Game Over')
			print ('correct guess: '+ str(len(cLetters)) + '\n missed guess: ' + str(len(mLetters)))
			gameOver = True
			print (' !!! you loose !!!\nthe secret word is ' +'\'' + secretWord + '\'')

	if gameOver:
		if playAgain ():
			mLetters = ''
			cLetters = ''
			secretWord = getRandomWord (words)
			gameOver = False

		else:
			break


















