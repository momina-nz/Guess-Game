# The Great Guessing Game

## Overview
The Great Guessing Game is a command-line word guessing game implemented in **Python 3.x**. The game allows users to either play by guessing a randomly chosen word letter by letter or test the game by directly seeing the word and trying to guess it.

## Features
- ✅ Users can choose between **Play Mode** and **Test Mode**.
- 🎯 Word selection is done randomly from a provided text file containing four-letter words.
- 🔠 Users can guess entire words or individual letters.
- 📊 Score tracking based on correct and incorrect guesses.
- 📜 A final report summarizing the game session.

## Files in the Repository

| File              | Description |
|------------------|-------------|
| `Game.py`        | Defines the `Game` class, which manages individual game instances. |
| `Guess.py`       | Contains the main game logic, allowing users to play and interact with the game. |
| `stringDatabase.py` | Handles word retrieval from `four_letters.txt`. |
| `words.py`       | Main entry point for running the game, parsing user commands, and initiating gameplay. |
| `four_letters.txt` | A text file containing a list of four-letter words used for the game. |

## Installation and Setup
### Prerequisites
- 🐍 **Python 3.x** (Ensure you are running the game in a Python 3 environment)

### Running the Game
1. **Clone the repository:**
[🔗 GitHub Repository: Guess Game](https://github.com/momina-nz/Guess-Game)
   ```sh
   git clone https://github.com/momina-nz/Guess-Game
   cd the-great-guessing-game
   ```
3. **Run the game in Play Mode:**
    ```sh
   python words.py play
   ```
4. **Run the game in Test Mode:**
   ```sh
   python words.py test
   ```
## How to play
🎮 The game will display the current word status with guessed letters filled in.

📌 **Actions:**
  - 🔡 `g` : Guess the full word.
  - 🔤 `l` : Guess a letter.
  - ❓ `t` : Give up and reveal the word.
  - ❌ `q` : Quit the game and see the final report.

📊 **Score Calculation:**
- Correct letter guesses **increase** the score.
- Incorrect guesses **incur a penalty**.
- Giving up **negatively impacts** the score.
  
## Example Gameplay
- ++
- ++ The great guessing game
- ++
- 
- Current Guess: ----
- Letters Guessed: a, e, i
- 
- g = guess, t = tell me, l for a letter, q to quit
- Enter Option: l
- Enter a letter: o
- @@ FEEDBACK: Woo Hoo, You found 1 letter(s)

## Notes
```markdown
- 🛠 The game does **not** require any external libraries beyond Python's standard modules.
- 📂 The files should be placed in the **same directory** and executed from there (no need for packages).
```

   
