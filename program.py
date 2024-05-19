# main.py
from person import Person

person = Person("Tom")
print(person)

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    num1 = 5
    num2 = 3
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")

value = 10
print(value)
