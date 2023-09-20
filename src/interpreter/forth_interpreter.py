from src.command.algebraic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from src.command.stack import DupCommand, DropCommand, SwapCommand, OverCommand
from src.base.custom_command import CustomCommand

class ForthInterpreter:
    def __init__(self):
        # The main stack for the Forth interpreter.
        self.stack = []
        
        # Dictionary to map words to their corresponding commands.
        self.commands = {
            '+': AddCommand(),
            '-': SubtractCommand(),
            '*': MultiplyCommand(),
            '/': DivideCommand(),
            'DUP': DupCommand(),
            'DROP': DropCommand(),
            'SWAP': SwapCommand(),
            'OVER': OverCommand()
        }
        
    def execute(self, input_str):
        """
        Parse and execute the given input string.
        """
        tokens = input_str.upper().split()
        
        # Process tokens to handle custom word definitions and execute other commands
        idx = 0
        while idx < len(tokens):
            token = tokens[idx]
            if token == ':':
                # Custom word definition starts
                word_name = tokens[idx + 1]
                definition_tokens = []
                idx += 2
                while tokens[idx] != ';':
                    definition_tokens.append(tokens[idx])
                    idx += 1
                self.commands[word_name] = CustomCommand(' '.join(definition_tokens))
                idx += 1  # Move past the ';'
            elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                self.stack.append(int(token))
                idx += 1
            elif token in self.commands:
                if isinstance(self.commands[token], CustomCommand):
                    # If it's a custom command, execute its definition
                    self.execute(self.commands[token].definition)
                else:
                    self.commands[token].execute(self.stack)
                idx += 1
            else:
                raise ValueError(f"undefined operation: {token}")
                
        return self.stack

# Testing the custom word definition and execution again
interpreter = ForthInterpreter()
print(interpreter.execute(": SQUARE DUP * ; 5 SQUARE"))  # Expected: [25]
