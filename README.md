# Forth Interpreter in Python

This project is a simple implementation of a subset of the Forth programming language in Python, motivated by the [Exercism challenge on Forth](https://exercism.org/tracks/python/exercises/forth). Forth is a stack-based, procedural, and extensible programming language. More details about the Forth language can be found on its [Wikipedia page](https://en.wikipedia.org/wiki/Forth_(programming_language)).

This implementation provides basic arithmetic operations, stack manipulations, and support for custom word definitions.

## Project Structure

```
.
├── solutions_comparation.md  # A document comparing two different approachs to the problem that this repository intend to solve (pt-br)
├── Makefile                  # Makefile for common operations
├── README.md                 # This documentation
├── poetry.lock               # Lock file for dependencies (managed by Poetry)
├── pyproject.toml            # Project metadata and dependencies (managed by Poetry)
├── src/                      # Source code
│   ├── base/                 # Base command classes
│   ├── command/              # Command implementations
│   └── interpreter/          # Main Forth interpreter
└── tests/                    # Unit tests
```

## Setup

1. Install [Poetry](https://python-poetry.org/docs/), a tool for dependency management and packaging in Python.

2. Navigate to the project root and install the dependencies:
   ```bash
   poetry install
   ```

## Usage

To use the Forth interpreter:

```python
from src.interpreter import ForthInterpreter

interpreter = ForthInterpreter()
result = interpreter.execute("5 3 +")
print(result)  # Outputs: [8]
```

## Supported Commands

- Arithmetic: `+`, `-`, `*`, `/`
- Stack Manipulations: `DUP`, `DROP`, `SWAP`, `OVER`
- Custom Word Definitions: `: word-name definition ;`

## Tests

Unit tests are available in the `tests/` directory. You can run them using:

```bash
poetry run pytest tests/
```
