# Kanye Says...

A Python GUI application that displays random Kanye West quotes using the Kanye REST API. The application is built with **Tkinter** for the graphical interface and **Requests** for fetching quotes from the API.

---

## Features

* Simple Tkinter-based graphical interface
* Fetches random Kanye West quotes in real time
* Updates the displayed quote with a single button click
* Uses custom background and button images

---

## Technologies Used

* Python 3
* Tkinter
* Requests
* Kanye REST API

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Kanye-Says.git
```

2. Navigate to the project directory:

```bash
cd Kanye-Says
```

3. Install the required dependency:

```bash
pip install requests
```

4. Run the application:

```bash
python main.py
```

---

## How It Works

1. The application launches with a default quote displayed.
2. Clicking the Kanye button sends a request to the Kanye REST API.
3. The API returns a random quote in JSON format.
4. The displayed text is updated automatically.

---

## Concepts Practiced

* GUI development with Tkinter
* Working with REST APIs
* JSON parsing
* Event-driven programming
* Canvas widgets
* Button callbacks
* Exception handling using `raise_for_status()`

---

## Requirements

* Python 3.x
* requests

Install the required package using:

```bash
pip install requests
```

---

## API Used

**Kanye REST API**

Provides random Kanye West quotes in JSON format.

