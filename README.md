# BookBot 📚

BookBot is a command-line application written in Python that analyzes text files and generates basic statistics about their contents.

It counts the total number of words and calculates the frequency of individual alphabetic characters, presenting the results in descending order.

## Features

- **Word Count** – Calculates the total number of words in a text file.
- **Character Frequency** – Counts how frequently each character appears in the text.
- **Case-Insensitive Analysis** – Treats uppercase and lowercase characters as the same character.
- **Sorted Results** – Displays character frequencies in descending order.
- **Command-Line Interface** – Accepts a text file path as a command-line argument.

## Tech Stack

- Python 3
- Standard Python Libraries

## Project Structure

```text
BookBot/
├── books/
│   └── book.txt
├── main.py
├── stats.py
└── README.md
```

| File / Directory | Description |
|---|---|
| `books/` | Contains text files to be analyzed. |
| `main.py` | Application entry point. Handles file reading and report generation. |
| `stats.py` | Contains functions for word counting, character counting, and sorting. |

## Getting Started

### Prerequisites

Make sure you have Python 3 installed on your machine.

Check your Python version:

```bash
python3 --version
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Permanaa/BookBot.git
```

2. Navigate to the project directory:

```bash
cd BookBot
```

### Usage

Run the application by providing the path to a text file:

```bash
python3 main.py books/book.txt
```

You can also analyze other `.txt` files by passing their paths as arguments:

```bash
python3 main.py books/frankenstein.txt
```

### Example Output

```text
====== BOOKBOT ======
Analyzing book found at books/frankenstein.txt...
------ Word Count ------
Found 75767 total words
------ Character Count ------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
...
====== END ======
```

---
