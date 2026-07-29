# Caesar Cipher

A Python command-line application that encrypts and decrypts messages using the **Caesar Cipher** technique. The program allows users to choose between encoding and decoding messages with a custom shift value while preserving unsupported characters.

## Features

- Encrypt messages using a custom shift value
- Decrypt encrypted messages
- Supports:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Special characters:
    - `! @ # $ % ^ & * < > ?`
- Preserves spaces, numbers, and any unsupported characters
- Uses modular arithmetic to wrap around the character list
- Interactive command-line interface
- Allows multiple encryption/decryption operations in a single session

## How It Works

The program stores all supported characters in a single list. During encryption or decryption:

- Each supported character is located in the list.
- For **encoding**, the shift value is added to its index.
- For **decoding**, the shift value is subtracted.
- The modulo (`%`) operator ensures the index wraps around when it reaches the end of the list.
- Characters not included in the list (such as spaces and numbers) remain unchanged.

## Technologies Used

- Python 3

```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/yourusername/Caesar-Cipher.git
```

2. Navigate to the project directory

```bash
cd Caesar-Cipher
```

3. Run the program

```bash
python main.py
```

## Example

```
Type 'encode' to encrypt, type 'decode' to decrypt
encode

Type your message
Hello World!

Type the shift number
5

Your encrypted message is:
Mjqqt<\twqiF
```

To decrypt:

```
Type 'encode' to encrypt, type 'decode' to decrypt
decode

Type your message
Mjqqt<\twqiF

Type the shift number
5

Your decrypted message is:
Hello World!
```

## Concepts Practiced

This project helped practice:

- Python functions
- Lists and indexing
- Loops (`for` and `while`)
- Conditional statements (`if`)
- String manipulation
- User input handling
- Modular arithmetic
- Building interactive command-line applications

## Future Improvements

- Validate user input for invalid operations
- Allow users to define their own character set
- Read messages from text files
- Save encrypted/decrypted messages to a file
- Add a graphical user interface (GUI)

## License

This project is open-source and available for learning and educational purposes.
