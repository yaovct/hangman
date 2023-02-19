# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:14:12 2023

@author: chttl200
"""
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    inputW = {}
    for i in secretWord:
        if i in lettersGuessed:
            inputW[i] = 1
        else:
            inputW[i] = 0
    if sum(inputW.values()) == len(inputW):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    inputW = {}
    out = ''
    for i in secretWord:
        if i in lettersGuessed:
            inputW[i] = i
        else:
            inputW[i] = '_'
    
    for i in secretWord:
        out += inputW[i]

    return out


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = list(a)
    for i in a:
        for j in lettersGuessed:
            if i == j and i in b:
                b.remove(i)
    
    return ''.join(b)


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
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long." % len(secretWord))
    lettersGuessed = []
    i = 0
    while i < 8:
        print("-----------")
        print("You have %d guesses left." % (8 - i))
        print("Available Letters: %s" % getAvailableLetters(lettersGuessed))
        s = input("Please guess a letter: ")
        if s in lettersGuessed:
            print("Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, lettersGuessed))
            i -= 1
        else:
            lettersGuessed.append(s)
            if s in secretWord:
                print("Good guess: %s" % getGuessedWord(secretWord, lettersGuessed))
                i -= 1
                if isWordGuessed(secretWord, lettersGuessed):
                    break
            else:
                print("Oops! That letter is not in my word: %s" % getGuessedWord(secretWord, lettersGuessed))
        i += 1
    
    print("-----------")
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was %s" % secretWord)
        
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)