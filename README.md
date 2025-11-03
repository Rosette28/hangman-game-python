# Hangman Python Game

## Description
This is a **classic Hangman** game built with **Python**. The game allows a user to guess a secret word one letter at a time. The user is given six attempts to guess the word before the game ends. The game is interactive and runs in the terminal with colorful ASCII art for the hangman as incorrect guesses accumulate.

## Features
- **Colorful Interface**: The game features a random color display for the welcome screen and hangman stages.
- **Word Selection**: The secret word is chosen from a word file that the user provides.
- **Interactive Gameplay**: Players input their guesses one letter at a time, and the current state of the word is displayed after each guess.
- **Hangman Visualization**: As incorrect guesses are made, a graphical hangman is displayed to show the player's progress.
- **Game Over Conditions**: The game ends when the player either guesses the word or exhausts their 6 attempts.

## Technologies Used
- **Python** (for game logic)
- **Libraries**:
  - `random`: For random color selection and word choice
  - `os`: For terminal color handling

## How to Play
1. Run the script `hangman.py` in your terminal or command line.
2. Enter the path of the words file (a `.txt` file with words separated by spaces).
3. Choose a word by specifying its position (e.g., "1" for the first word in the file).
4. Guess letters one at a time. Each incorrect guess will be shown with an updated hangman graphic.
5. Try to guess the word within six incorrect guesses!

## Installation
To run the game locally:
1. Clone or download the repository.
2. Navigate to the project directory in your terminal.
3. Run the Python script:
   ```bash
   python hangman.py

## About the Project
This Hangman game was created when I was **13 years old** as the **final project for a Python programming course**.  
It represents my early steps into programming and my enthusiasm for building interactive terminal games.
