# 🎯 Number Guessing Game

A simple command-line **Number Guessing Game** built with Python. The computer randomly selects a number between **1 and 100**, and your goal is to guess it before you run out of lives.

---

## 📌 Features

- 🎲 Random number generation using Python's `random` module
- 🎮 Two difficulty levels:
  - **Easy** – 10 lives
  - **Hard** – 5 lives
- 📉 Gives hints after each guess:
  - Too High
  - Too Low
- 🏆 Winning and losing conditions
- 💻 Beginner-friendly command-line interface

---

## 🛠️ Technologies Used

- Python 3
- Random Module

---

## ▶️ How to Run

1. Clone this repository

```bash
git clone https://github.com/your-username/number_guessing_game.git
```

2. Navigate to the project folder

```bash
cd number_guessing_game
```

3. Run the program

```bash
python main.py
```

---

## 🎮 Gameplay

1. The computer chooses a random number between **1 and 100**.
2. Select a difficulty level:
   - Easy (10 lives)
   - Hard (5 lives)
3. Enter your guess.
4. The game will tell you whether your guess is:
   - 📈 Too High
   - 📉 Too Low
5. Keep guessing until:
   - You guess the correct number 🎉
   - You run out of lives 💀

---

## 📸 Sample Output

```
Welcome to Number Guessing Game!

I am thinking of a number between 1 and 100.

Choose a level: Easy / Hard
easy

You have 10 lives left.

Guess the number:
50

Too High!
Guess Again.

You have 9 lives left.

Guess the number:
25

Too Low!
Guess Again.

You have 8 lives left.

Guess the number:
37

You guessed right! The number was 37.
```

---

## 🚀 Future Improvements

- Input validation for invalid entries
- Play Again option
- Score tracking
- Multiple difficulty levels
- Statistics (games played, wins, losses)
- Graphical User Interface (Tkinter/Pygame)

---

## 🎯 Learning Outcomes

This project helped practice:

- Variables
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`while`)
- User Input
- Random Number Generation
- Basic Game Logic
- Python Functions and Flow Control

