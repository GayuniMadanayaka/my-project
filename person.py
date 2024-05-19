# person.py

class Person:
    """A simple class to represent a person."""

    def __init__(self, name):
        """Initialize the person with a name."""
        self.name = name

    def print_name(self):
        """Print the person's name."""
        print(f"Hello, my name is {self.name}.")

if __name__ == "__main__":
    person = Person("Alice")
    person.print_name()
