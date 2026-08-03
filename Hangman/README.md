# 🎮 Hangman Game

A classic **Hangman** game built in Python that runs in the terminal. Guess the hidden word one letter at a time before the hangman is fully drawn. Every incorrect guess costs one life, so choose wisely!

---

## 📌 Features

* Randomly selects a word each game
* Interactive command-line gameplay
* ASCII art title and hangman illustrations
* Six lives to guess the word
* Reveals correctly guessed letters
* Displays the secret word if the player loses
* Simple and beginner-friendly Python project

---

## 🛠️ Built With

* Python 3
* Built-in `random` module

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your computer

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/hangman-game.git
```

Move into the project directory:

```bash
cd hangman-game
```

Run the game:

```bash
python main.py
```

---

## 🎯 Gameplay

When the game starts, a random word is chosen and displayed as underscores.

Example:

```text
Word: _ _ _ _ _
```

Enter a letter:

```text
Guess the letter:
> a
```

* ✅ Correct guess → The letter is revealed.
* ❌ Wrong guess → You lose one life, and another part of the hangman appears.

Win by guessing every letter before your six lives run out.

---

## 💻 Example

```text
_ _ _ _ _

Guess the letter:
> e

_e__e

Life remaining: 5/6
```

---

## 📂 Project Structure

```text
hangman-game/
│
├── main.py
└── README.md
```

---

## 🧠 Concepts Practiced

* Variables
* Loops (`while`, `for`)
* Conditional statements
* Lists
* Strings
* User input
* Randomization
* Basic game development
* ASCII art

---

## 🔮 Future Enhancements

* Multiple difficulty levels
* Word categories
* Multiplayer mode
* Scoreboard
* Hints
* Replay option
* Input validation
* Colored terminal output

---

## 📖 What I Learned

While building this project, I practiced creating a complete command-line game using Python. It strengthened my understanding of loops, conditionals, list operations, string manipulation, and implementing game logic while making the experience interactive for the player.

