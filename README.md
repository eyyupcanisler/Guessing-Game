# Guessing Game README

## Introduction:
Welcome to the Guessing Game! This simple Python program allows users to guess a randomly generated number within a specified range. The game provides feedback on the closeness of the guesses and limits the number of attempts based on the range chosen by the user.

## Instructions:
1. Run the Python script to start the game.
2. Follow the instructions prompted by the program to set the lower and upper limits for the range within which the random number will be generated.
3. Make guesses to find the randomly generated number.
4. Based on your guesses, the program will provide feedback on whether you are close or far from the correct answer.
5. You have a limited number of guesses based on the range you selected. Make them count!
6. If you guess the number correctly within the allowed attempts, you win! Otherwise, the game ends in failure.

## Game Rules:
- The lower limit should be equal to or greater than 0, and the upper limit should be equal to or less than 100.
- The number of guesses allowed varies based on the range selected:
  - Range < 0-9: 2 guesses
  - Range between 10-19: 4 guesses
  - Range between 20-39: 6 guesses
  - Range between 40-100: 8 guesses
- If a guess is far from the correct answer (difference >= 10), the program will advise you to "Go up a lot" or "Go down a lot".
- If a guess is close to the correct answer (difference < 10), the program will advise you to "Go up a bit" or "Go down a bit".
- The number of remaining guesses will be displayed after each guess.
- If you use all your guesses without finding the correct answer, the game ends in failure.

## Dependencies:
- Python 3.x

## How to Run:
1. Ensure you have Python installed on your system.
2. Download the Python script (`guessing_game.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script using the command `python guessing_game.py`.
6. Follow the on-screen instructions to play the game.

