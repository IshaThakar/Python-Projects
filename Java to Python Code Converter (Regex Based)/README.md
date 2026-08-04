# Java to Python Code Converter (Regex Based)

## Overview

This project is a simple Java-to-Python code converter built using Python and Regular Expressions (`re` module). It reads Java source code from a file, detects specific Java syntax, and converts it into equivalent Python syntax.

The project demonstrates how regular expressions can be used for basic source code transformation.

## Features

* Converts `System.out.println()` to Python `print()`
* Converts `System.out.print()` to Python `print(..., end="")`
* Converts basic Java `for` loops into Python `range()` loops
* Reads Java code from an input file
* Produces converted Python-style code


## Supported Conversions

### Print Statements

#### Java

```java
System.out.println("Hello");
```

#### Python

```python
print("Hello")
```

---

#### Java

```java
System.out.print("Hello");
```

#### Python

```python
print("Hello", end="")
```

---

### For Loops

#### Java

```java
for(int i = 0; i < 5; i++)
```

#### Python

```python
for i in range(0, 5):
```

## How It Works

1. Reads Java code from `input.java`.
2. Uses regular expressions to identify Java syntax.
3. Replaces matching patterns with Python equivalents.
4. Prints the converted code.

## Requirements

* Python 3.x

No external libraries are required.

## Running the Project

```bash
python converter.py
```

## Current Limitations

This project is intended for learning purposes and currently supports only a subset of Java syntax.

Current limitations include:

* Only basic `for` loops are supported.
* Does not convert `while` or enhanced `for-each` loops.
* Does not convert `if`, `else`, `switch`, or methods.
* Braces (`{}`) are not removed.
* Python indentation is not generated.
* Does not support `printf()` statements.
* Complex loop conditions are not handled.

## Future Improvements

* Support `while` loops
* Support `if-else` statements
* Convert variable declarations
* Remove Java braces automatically
* Generate proper Python indentation
* Convert functions and classes
* Support arrays and collections
* Add command-line arguments for input/output files

## Concepts Used

* Python File Handling
* Regular Expressions (`re`)
* Pattern Matching
* Nested Functions
* String Manipulation
* Code Transformation
