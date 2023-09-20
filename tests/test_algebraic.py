from src.command.algebraic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    stack = [5, 3]
    cmd = AddCommand()
    cmd.execute(stack)
    assert stack == [8], f"Expected [8], but got {stack}"

def test_subtract_command():
    stack = [5, 3]
    cmd = SubtractCommand()
    cmd.execute(stack)
    assert stack == [2], f"Expected [2], but got {stack}"

def test_multiply_command():
    stack = [5, 3]
    cmd = MultiplyCommand()
    cmd.execute(stack)
    assert stack == [15], f"Expected [15], but got {stack}"

def test_divide_command():
    stack = [5, 2]
    cmd = DivideCommand()
    cmd.execute(stack)
    assert stack == [2], f"Expected [2], but got {stack}"
