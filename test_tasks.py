import pytest
from tasks import (
    Vehicle, BankAccount, Dog, Student, MathOperations,
    Temperature, Vector, Book, JsonMixin, Shape, Circle
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

def test_student_from_string():
    student = Student.from_string("Alice Smith,90,85,88")
    assert student.name == "Alice Smith"
    assert student.grades == [90, 85, 88]
  
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

def test_json_mixin():
    class TestClass(JsonMixin):
        def __init__(self, a, b):
            self.a = a
            self.b = b
    obj = TestClass(1, 2)
    assert obj.to_json() == '{"a": 1, "b": 2}'

def test_shape_subclass():
    circle = Circle(5)
    assert circle.area() == pytest.approx(78.54, 0.01)
    assert circle.perimeter() == pytest.approx(31.42, 0.01)
