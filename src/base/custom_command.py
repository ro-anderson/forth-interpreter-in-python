from src.base.command import Command

class CustomCommand(Command):
    """
    Concrete command class for custom defined words.
    """
    def __init__(self, definition):
        self.definition = definition
        
    def execute(self, interpreter):
        # Recursively call the interpreter to execute the custom word's definition.
        interpreter.execute(self.definition)