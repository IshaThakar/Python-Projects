# Personalized Invitation Letter Generator

A simple Python automation project that generates personalized invitation letters for multiple people by replacing the `[name]` placeholder in a letter template.

## Description

The program reads a list of names from `invited_names.txt` and a letter template from `starting_letter.txt`. It replaces `[name]` with each person's name and creates a separate personalized letter for every recipient.

This eliminates the need to manually edit the letter for each person.

## How It Works

1. Reads all names from `invited_names.txt`.
2. Reads the letter template from `starting_letter.txt`.
3. Removes extra whitespace from each name.
4. Replaces `[name]` with the current name.
5. Creates a personalized letter for each recipient.
6. Saves the generated letters in the output folder.

## Example

If the template contains:

```text
Dear [name],

You are invited to our special event.
```

And the names file contains:

```text
Alice
Bob
Charlie
```

The program generates personalized letters such as:

```text
Dear Alice,

You are invited to our special event.
```

## Technologies Used

* Python
* File handling
* String manipulation
* Loops
* F-strings

## How to Run

Make sure Python is installed and run:

```bash
python main.py
```

The personalized letters will be generated in the `output/ReadyToSend/` folder.

## Future Improvements

* Use `python-docx` to generate actual Word documents.
* Add email automation to send the generated letters.
* Support multiple placeholders such as `[name]`, `[date]`, and `[event]`.
* Add error handling for missing files or folders.



