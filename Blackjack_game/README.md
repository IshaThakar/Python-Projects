# Blackjack

A command-line implementation of the classic Blackjack card game built using Python. Play against the computer dealer and test your luck while following standard Blackjack rules.

## Features

- Interactive command-line gameplay
- Random card generation
- Dealer AI
- Automatic score calculation
- Blackjack detection
- Bust detection
- Multiple rounds of play

## Technologies Used

- Python 3
- Random module

## Game Rules

- Both the player and dealer receive two cards.
- Number cards are worth their face value.
- Face cards (J, Q, K) are worth 10.
- Ace can count as 11 or 1 depending on the hand.
- Player chooses to:
  - Hit (draw another card)
  - Stand (keep current hand)
- Dealer draws until reaching at least 17.
- Highest score without exceeding 21 wins.

## Example Gameplay

```text
Your cards: [10, 8]
Current score: 18

Dealer's first card: 9

Type 'y' to hit or 'n' to stand:
n

Dealer's cards: [9, 7, 5]
Dealer score: 21

You lose.
```
## Future Improvements

- Card graphics using Unicode
- Betting system
- Multiple decks
- Player statistics
- Difficulty levels
- GUI version with Tkinter or Pygame

## Learning Outcomes

This project helped practice:

- Lists
- Functions
- Loops
- Conditional statements
- Random module
- Game logic
- Score calculation
- Python programming fundamentals

