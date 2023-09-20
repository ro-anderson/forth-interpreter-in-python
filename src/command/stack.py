from src.base.command import Command

class DupCommand(Command):
    """
    Concrete command class for DUP operation (duplicates the top item on the stack).
    """
    def execute(self, stack):
        if len(stack) < 1:
            raise StackUnderflowError("Insufficient number of items in stack for DUP operation.")
        stack.append(stack[-1])

class DropCommand(Command):
    """
    Concrete command class for DROP operation (removes the top item from the stack).
    """
    def execute(self, stack):
        if len(stack) < 1:
            raise StackUnderflowError("Insufficient number of items in stack for DROP operation.")
        stack.pop()

class SwapCommand(Command):
    """
    Concrete command class for SWAP operation (swaps the top two items).
    """
    def execute(self, stack):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack for SWAP operation.")
        stack[-1], stack[-2] = stack[-2], stack[-1]

class OverCommand(Command):
    """
    Concrete command class for OVER operation (copies the second item to the top).
    """
    def execute(self, stack):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack for OVER operation.")
        stack.append(stack[-2])

