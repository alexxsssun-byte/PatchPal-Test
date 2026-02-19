def greet(name):
    """Return a greeting message."""
    return f"Goodbye, {name}!"  # BUG: should be Hello

def farewell(name):
    """Return a farewell message."""
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet("World"))
