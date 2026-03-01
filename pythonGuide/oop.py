"""
PYTHON OBJECT ORIENTED PROGRAMMING (OOP) - COMPLETE GUIDE
Author: Your Name
Purpose: Teach OOP concepts from beginner → advanced level

OOP is used everywhere in real software and ML frameworks.

Core concepts:
1. Class
2. Object
3. Attributes
4. Methods
5. Constructor
6. Encapsulation
7. Inheritance
8. Polymorphism
"""


# ============================================================
# SECTION 1: BASIC CLASS AND OBJECT
# ============================================================

print("\n--- SECTION 1: Basic Class and Object ---")

# Class = blueprint
class Student:

    # class attribute (shared by all objects)
    school = "Northwood University"

    # method
    def greet(self):
        print("Hello, I am a student")


# Object = instance of class
student1 = Student()
student1.greet()

print(student1.school)


# ============================================================
# SECTION 2: CONSTRUCTOR (__init__)
# ============================================================

print("\n--- SECTION 2: Constructor ---")

class Person:

    # constructor runs automatically when object is created
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# create object
person1 = Person("Mayura", 20)
person1.display()


# ============================================================
# SECTION 3: INSTANCE ATTRIBUTES AND METHODS
# ============================================================

print("\n--- SECTION 3: Instance Attributes and Methods ---")

class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)

    def accelerate(self):
        self.speed += 10
        print("New speed:", self.speed)


car1 = Car("Toyota", 100)

car1.show_info()
car1.accelerate()


# ============================================================
# SECTION 4: ENCAPSULATION (Protect data)
# ============================================================

print("\n--- SECTION 4: Encapsulation ---")

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Mayura", 1000)

account.deposit(500)

# Cannot access directly:
# print(account.__balance)  # ERROR

# Must use method
print("Balance:", account.get_balance())


# ============================================================
# SECTION 5: INHERITANCE
# ============================================================

print("\n--- SECTION 5: Inheritance ---")

# Parent class
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes sound")


# Child class inherits Animal
class Dog(Animal):

    def speak(self):
        print(self.name, "barks")


dog = Dog("Buddy")

dog.speak()


# ============================================================
# SECTION 6: POLYMORPHISM
# ============================================================

print("\n--- SECTION 6: Polymorphism ---")

class Cat(Animal):

    def speak(self):
        print(self.name, "meows")


animals = [Dog("Rex"), Cat("Kitty")]

for animal in animals:
    animal.speak()

# Same method name, different behavior


# ============================================================
# SECTION 7: CLASS VARIABLES VS INSTANCE VARIABLES
# ============================================================

print("\n--- SECTION 7: Class vs Instance variables ---")

class Employee:

    company = "Google"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable


emp1 = Employee("Alice")
emp2 = Employee("Bob")

print(emp1.company)
print(emp2.company)


# ============================================================
# SECTION 8: STATIC METHODS
# ============================================================

print("\n--- SECTION 8: Static Methods ---")

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


result = MathUtils.add(5, 3)
print("Result:", result)


# ============================================================
# SECTION 9: CLASS METHODS
# ============================================================

print("\n--- SECTION 9: Class Methods ---")

class University:

    name = "Default University"

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name


University.change_name("Northwood University")

print(University.name)


# ============================================================
# SECTION 10: REAL-WORLD EXAMPLE (ML MODEL SIMULATION)
# ============================================================

print("\n--- SECTION 10: ML Model Example ---")

class MLModel:

    def __init__(self, model_name):
        self.model_name = model_name
        self.is_trained = False

    def train(self):
        print("Training model:", self.model_name)
        self.is_trained = True

    def predict(self):
        if not self.is_trained:
            print("Error: Model not trained")
        else:
            print("Making predictions using", self.model_name)


model = MLModel("House Price Predictor")

model.predict()

model.train()

model.predict()


# ============================================================
# SECTION 11: MAGIC METHODS (__str__)
# ============================================================

print("\n--- SECTION 11: Magic Methods ---")

class Book:

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book title is {self.title}"


book = Book("Python Guide")

print(book)


# ============================================================
# SUMMARY
# ============================================================

"""
KEY CONCEPTS SUMMARY:

Class = blueprint
Object = instance of class
__init__ = constructor
self = refers to current object

Encapsulation = protect data
Inheritance = reuse code
Polymorphism = same method, different behavior

Static method = utility function
Class method = modifies class state

OOP is used in:
- ML frameworks (PyTorch, TensorFlow)
- Web frameworks
- Game development
- Backend systems
"""

print("\nOOP guide complete.")