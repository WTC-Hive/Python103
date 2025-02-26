# Task 1: Create a Basic Class
class Vehicle:
    """
    Create a Vehicle class with the following attributes:
    - make (string)
    - model (string)
    - year (integer)
    Initialize these attributes via the constructor.
    """
    pass

# Task 2: Add Methods to a Class
class BankAccount:
    """
    Create a BankAccount class with:
    - balance (float, initialized to 0)
    - Methods: deposit(amount), withdraw(amount), and get_balance().
    Withdrawing more than the balance should raise a ValueError.
    """
    pass

# Task 3: Inheritance
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    """
    Inherit from Animal and override speak() to return "Woof!".
    """
    pass

# Task 4: Class Methods
class Student:
    """
    Create a Student class with:
    - name (string)
    - grades (list of integers)
    - A class method `from_string(cls, string)` that creates a Student instance 
      from a string like "John Doe,85,90,78".
    """
    pass

# Task 5: Static Methods
class MathOperations:
    """
    Add static methods:
    - add(a, b): returns a + b
    - factorial(n): returns the factorial of n (use a loop).
    """
    pass

# Task 6: Properties and Setters
class Temperature:
    """
    Create a Temperature class with a private attribute _celsius.
    Add a property `celsius` and a property `fahrenheit` that converts between Celsius and Fahrenheit.
    (Formula: F = C * 9/5 + 32)
    """
    pass

# Task 7: Operator Overloading
class Vector:
    """
    Create a Vector class with x and y attributes.
    Overload the `+` operator to add two Vector instances.
    """
    pass

# Task 8: Class with Exception Handling
class Book:
    """
    Create a Book class with:
    - title (string)
    - author (string)
    The constructor should raise a ValueError if title or author is empty.
    """
    pass

# Task 9: Mixin Class
class JsonMixin:
    """
    Create a JsonMixin class with a method to_json() that returns a JSON string 
    of the object's __dict__.
    """
    pass

# Task 10: Abstract Base Class
from abc import ABC, abstractmethod
class Shape(ABC):
    """
    Create an abstract Shape class with:
    - An abstract method area()
    - An abstract method perimeter()
    Create a subclass Circle that implements these methods.
    """
    pass
