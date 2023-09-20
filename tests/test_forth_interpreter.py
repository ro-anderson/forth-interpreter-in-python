from src.interpreter.forth_interpreter import ForthInterpreter

def test_forth_interpreter_basic_operations():
    # Testing addition
    interpreter = ForthInterpreter()
    result = interpreter.execute("5 3 +")
    assert result == [8], f"Expected [8], but got {result}"
    
    # Testing subtraction
    interpreter = ForthInterpreter()
    result = interpreter.execute("5 3 -")
    assert result == [2], f"Expected [2], but got {result}"
    
    # Testing multiplication
    interpreter = ForthInterpreter()
    result = interpreter.execute("5 3 *")
    assert result == [15], f"Expected [15], but got {result}"
    
    # Testing division
    interpreter = ForthInterpreter()
    result = interpreter.execute("5 2 /")
    assert result == [2], f"Expected [2], but got {result}"

def test_forth_interpreter_stack_manipulations():
    # Testing DUP
    interpreter = ForthInterpreter()
    result = interpreter.execute("5 3 DUP")
    assert result == [5, 3, 3], f"Expected [5, 3, 3], but got {result}"
    
    # Testing DROP
    interpreter = ForthInterpreter()
    result = interpreter.execute("5 3 DROP")
    assert result == [5], f"Expected [5], but got {result}"
    
    # Testing SWAP
    interpreter = ForthInterpreter()
    result = interpreter.execute("5 3 SWAP")
    assert result == [3, 5], f"Expected [3, 5], but got {result}"
    
    # Testing OVER
    interpreter = ForthInterpreter()
    result = interpreter.execute("5 3 OVER")
    assert result == [5, 3, 5], f"Expected [5, 3, 5], but got {result}"

def test_forth_interpreter_custom_word_definitions():
    # Testing custom word definition and execution
    interpreter = ForthInterpreter()
    result = interpreter.execute(": SQUARE DUP * ; 5 SQUARE")
    assert result == [25], f"Expected [25], but got {result}"
    
    # Testing custom word within another custom word definition
    interpreter = ForthInterpreter()
    result = interpreter.execute(": DOUBLE 2 * ; : QUADRUPLE DOUBLE DOUBLE ; 5 QUADRUPLE")
    assert result == [20], f"Expected [20], but got {result}"