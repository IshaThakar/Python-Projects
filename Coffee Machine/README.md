# Coffee Machine Simulator

A Python-based Coffee Machine Simulator that replicates the basic functionality of a coffee vending machine. Users can order different coffee types, insert virtual coins, receive change, and monitor the available resources and cash balance.

---

## Features

- Order three types of coffee:
  - Espresso
  - Latte
  - Cappuccino
- Coin-based payment system
- Automatic change calculation
- Resource availability check
- Automatic resource refill when ingredients run out
- View machine resource and cash report
- Input validation for invalid commands

---

## Technologies Used

- Python 3
- Functions
- Dictionaries
- Loops
- Conditional Statements

---

## Menu

| Coffee | Price |
|--------|------:|
| Espresso | $1.50 |
| Latte | $2.50 |
| Cappuccino | $3.00 |

---

## Initial Resources

| Resource | Quantity |
|----------|---------:|
| Water | 300 ml |
| Milk | 200 ml |
| Coffee | 100 g |

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/yourusername/Coffee_Machine.git
```

2. Navigate to the project directory.

```bash
cd Coffee_Machine
```

3. Run the program.

```bash
python coffee_machine.py
```

---

## Example Usage

```text
What would you like? (espresso/latte/cappuccino)

latte

Please, insert coins.
How many pennies? 0
How many nickels? 0
How many dimes? 0
How many quarters? 10

Total: $2.50

Here's your order. Enjoy it!
```

---

## Available Commands

| Command | Description |
|----------|-------------|
| espresso | Order an Espresso |
| latte | Order a Latte |
| cappuccino | Order a Cappuccino |
| report | Display available resources and total cash |

---

## How It Works

1. The user selects a coffee.
2. The machine checks whether sufficient ingredients are available.
3. If resources are insufficient, the machine automatically refills them.
4. The user inserts coins until the required amount is reached.
5. The machine:
   - Calculates the payment.
   - Returns change if necessary.
   - Dispenses the selected coffee.
   - Updates the remaining resources.
   - Adds the payment to the cash register.

---

## Concepts Practiced

- Nested dictionaries
- Functions
- Loops (`while`)
- Conditional statements (`if`, `elif`, `else`)
- User input handling
- Resource management
- Payment processing
- Console-based application development

---

## Future Improvements

- Add more beverage options
- Store resources using files or a database
- Build a graphical user interface (GUI)
- Add an administrator mode for refilling resources
- Support digital payment methods
- Maintain transaction history
- Improve input validation and error handling

---

## Learning Outcomes

This project demonstrates how Python can be used to simulate a real-world coffee vending machine by combining functions, loops, dictionaries, and conditional logic. It also provides practical experience with resource management, user interaction, and payment handling in a console application.

