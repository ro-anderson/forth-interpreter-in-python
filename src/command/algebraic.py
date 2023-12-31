from src.base.command import Command

class AddCommand(Command):
    """
    Command class for addition operation.
    """
    def execute(self, stack):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack for addition operation.")
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)

class SubtractCommand(Command):
    """
    Command class for subtraction operation.
    """
    def execute(self, stack):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack for subtraction operation.")
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)

class MultiplyCommand(Command):
    """
    Command class for multiplication operation.
    """
    def execute(self, stack):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack for multiplication operation.")
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)

class DivideCommand(Command):
    """
    Command class for division operation.
    """
    def execute(self, stack):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack for division operation.")
        b = stack.pop()
        if b == 0:
            raise ZeroDivisionError("divide by zero")
        a = stack.pop()
        stack.append(a // b)  # Integer division

    
