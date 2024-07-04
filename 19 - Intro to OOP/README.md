### Introduction to Object-Oriented Programming (OOP) in Python

#### What is Object-Oriented Programming (OOP)?
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data and code that manipulates that data. OOP aims to implement real-world entities like inheritance, hiding, polymorphism, etc., in programming. The main focus is on objects rather than functions or procedures.

#### Key Concepts in OOP:
1. **Class**: A blueprint for creating objects (a particular data structure), defining a set of attributes and methods.
2. **Object**: An instance of a class. When a class is defined, no memory is allocated until an object of that class is created.
3. **Attributes**: Variables that belong to an object or class. They represent the state or data of an object.
4. **Methods**: Functions that belong to an object or class. They define the behaviors or actions of an object.

#### Classes in Python
A class is defined using the `class` keyword followed by the class name and a colon. The class body contains attributes and methods.

```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
```

#### Objects in Python
An object is created using the class name followed by parentheses. This is called instantiation.

```python
# Instantiate the Dog class
my_dog = Dog("Buddy", 3)

# Accessing attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3

# Calling methods
print(my_dog.description())  # Output: Buddy is 3 years old.
print(my_dog.speak("Woof Woof"))  # Output: Buddy says Woof Woof
```

#### Attributes
Attributes are variables that hold data associated with an object or class. There are two types of attributes:

1. **Instance Attributes**: Defined inside the `__init__` method and unique to each instance.
2. **Class Attributes**: Defined inside the class but outside any methods, shared among all instances of the class.

```python
class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model):
        # Instance attributes
        self.make = make
        self.model = model
```

#### Methods
Methods are functions defined within a class. They are used to define the behaviors of an object.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Instantiate the Circle class
my_circle = Circle(5)

# Calling methods
print(my_circle.area())      # Output: 78.5
print(my_circle.perimeter()) # Output: 31.400000000000002
```

### Summary
- **Class**: Blueprint for creating objects.
- **Object**: An instance of a class.
- **Attributes**: Variables that hold data.
- **Methods**: Functions that define behaviors.

OOP helps in organizing code and making it more modular, reusable, and easier to maintain. By encapsulating data and functions that operate on that data into objects, OOP provides a clear structure for programs.