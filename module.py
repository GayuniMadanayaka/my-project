# module.py

class Module:
    """A simple class to represent a person."""

    def __init__(self, code):
        """Initialize the person with a name."""
        self.code = code

    def print_name(self):
        """Print the person's name."""
        print(f"Hello, my module is {self.code}.")

if __name__ == "__main__":
    module = Module("Maths")
    module.print_name()
