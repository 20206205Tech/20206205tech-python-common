def reverse_string(s: str) -> str:
    """Reverses a string."""
    return s[::-1]


def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}! Welcome to 20206205tech-python-common."


if __name__ == "__main__":
    print(greet("Developer"))
    print(f"Reversed 'Python': {reverse_string('Python')}")
