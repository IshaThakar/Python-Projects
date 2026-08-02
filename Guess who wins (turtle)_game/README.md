# Turtle Race Game

## Overview

Turtle Race Game is a simple Python project built using the `turtle` graphics module. The player places a bet by choosing the color of a turtle before the race begins. Six turtles then race across the screen with randomly generated movement until one crosses the finish line. The game announces whether the player's prediction was correct.

## Features

* Interactive color betting before the race starts.
* Six turtles with different colors.
* Randomized movement for each turtle.
* Declares the winning turtle.
* Displays whether the player won or lost the bet.

## Technologies Used

* Python
* Turtle Graphics
* Random Module

## How It Works

1. The program asks the player to enter the color of the turtle they think will win.
2. Six turtles are placed at the starting line.
3. Each turtle moves forward by a random distance during every iteration.
4. The race continues until one turtle reaches the finish line.
5. The program compares the winner's color with the player's bet and prints the result.

## Available Turtle Colors

* Red
* Yellow
* Blue
* Green
* Purple
* Cyan

## Requirements

* Python 3.x

No external libraries are required since both `turtle` and `random` are included with Python.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Turtle-Race-Game.git
```

Navigate to the project folder:

```bash
cd Turtle-Race-Game
```

Run the program:

```bash
python main.py
```

## Sample Output

```
MAKE YOUR BET!!
Which turtle will win the race? Enter a colour: blue

YOU WIN!!! the winner is blue
```

or

```
MAKE YOUR BET!!
Which turtle will win the race? Enter a colour: red

YOU LOSE!!! the winner is green
```

## Learning Outcomes

This project demonstrates:

* Working with the `turtle` graphics library.
* Creating multiple objects using loops.
* Storing objects in lists.
* Handling user input.
* Using the `random` module for simulation.
* Implementing game loops and conditional logic.

## Future Improvements

* Add a graphical winner announcement.
* Validate user input for invalid colors.
* Allow users to choose the number of turtles.
* Add a restart option after each race.
* Display race statistics and win history.


