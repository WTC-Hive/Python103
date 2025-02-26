import pytest
from tasks import (
    Vehicle, BankAccount, Dog, MathOperations,
    Temperature, Vector, Book
)

def test_vehicle_initialization():
    car = Vehicle("Toyota", "Camry", 2020)
    assert car.make == "Toyota"
    assert car.model == "Camry"
    assert car.year == 2020

def test_bank_account():
    acc = BankAccount()
    acc.deposit(100)
    assert acc.get_balance() == 100
    acc.withdraw(50)
    assert acc.get_balance() == 50
    with pytest.raises(ValueError):
        acc.withdraw(100)

def test_dog_speak():
    dog = Dog()
    assert dog.speak() == "Woof!"

def test_math_operations():
    assert MathOperations.add(2, 3) == 5
    assert MathOperations.factorial(5) == 120

def test_temperature_conversion():
    temp = Temperature(25)
    assert temp.fahrenheit == 77.0

def test_vector_addition():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    result = v1 + v2
    assert result.x == 4
    assert result.y == 6

def test_book_exception():
    with pytest.raises(ValueError):
        Book("", "J.K. Rowling")
    with pytest.raises(ValueError):
        Book("Harry Potter", "")
