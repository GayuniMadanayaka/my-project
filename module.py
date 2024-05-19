# module.py

class Module:
    """A simple class to represent a person."""

    def __init__(self, name):
        """Initialize the person with a name."""
        self.name = name

    def print_name(self):
        """Print the person's name."""
        print(f"Hello, my module is {self.name}.")

if __name__ == "__main__":
    module = Module("Maths")
    module.print_name()
