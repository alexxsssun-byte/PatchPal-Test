def add(a, b):
    """Add two numbers."""
    return a - b  # BUG: uses subtraction instead of addition

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    return a / b  # BUG: no zero-division check

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"5 * 6 = {multiply(5, 6)}")
    print(f"10 / 0 = {divide(10, 0)}")
