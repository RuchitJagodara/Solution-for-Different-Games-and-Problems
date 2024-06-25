# HangMan-Game
This repo contains the solver of hangman game which can predict unseen words with an accuracy of ~55% and seen words with an accuracy of >95%.

## How to try out the game

Just download the ipynb file and run all the cells. If you want, my statistical model play the game then just do computer = True (in the last cell) and if you want to try out just put a random word as the first argument in the play_game method and do computer = False, this will select a random word from a dictionary and you can play the game as you generally play the hangman game.

## What is hangman

You can check out the game from [here](https://en.wikipedia.org/wiki/Hangman_(game)).

## Algorithm used

I have used [N-gram](https://en.wikipedia.org/wiki/Word_n-gram_language_model) models to solve the problem.
