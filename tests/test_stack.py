from src.command.stack import DupCommand, DropCommand, SwapCommand, OverCommand

def test_dup_command():
    stack = [5, 3]
    cmd = DupCommand()
    cmd.execute(stack)
    assert stack == [5, 3, 3], f"Expected [5, 3, 3], but got {stack}"

def test_drop_command():
    stack = [5, 3]
    cmd = DropCommand()
    cmd.execute(stack)
    assert stack == [5], f"Expected [5], but got {stack}"

def test_swap_command():
    stack = [5, 3]
    cmd = SwapCommand()
    cmd.execute(stack)
    assert stack == [3, 5], f"Expected [3, 5], but got {stack}"

def test_over_command():
    stack = [5, 3]
    cmd = OverCommand()
    cmd.execute(stack)
    assert stack == [5, 3, 5], f"Expected [5, 3, 5], but got {stack}"
