Hangman Game
This is a Python implementation of the game Hangman. The game prompts the user to guess a word letter by letter until they either successfully guess the word or run out of attempts.

Usage
To run the game, call the function hangman(secretWord) where secretWord is the word that the player must guess.

The game will start by displaying the length of the word and the number of guesses remaining. The player will be prompted to guess a letter. If the letter is in the word, the game will update the display to show the partially guessed word and inform the player they made a good guess. If the letter is not in the word, the game will inform the player that the guess was incorrect and display the partially guessed word.

If the player has already guessed a letter, the game will inform them that the letter has already been guessed and not count that guess against them.

The game ends when the player has either guessed the word or run out of guesses. If the player guessed the word, the game will display a congratulations message. If the player ran out of guesses, the game will display a message indicating the word that was being guessed.
