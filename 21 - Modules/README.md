#### Modules

**Definition and Importance**

**What is a module?**
- A module is a file containing Python code that defines functions, classes, and variables. It can also include runnable code.
- Modules allow you to logically organize your Python code, making it easier to manage and reuse.

**Why use modules?**
- **Code Reusability:** Modules allow you to reuse code across multiple programs.
- **Code Organization:** Breaking down a program into smaller, manageable parts.
- **Namespace Management:** Modules help avoid naming conflicts by providing a separate namespace for different parts of your code.
- **Maintainability:** Easier to debug and maintain small modules compared to a large monolithic program.

**Creating a Module**

**Writing and saving a Python file as a module:**
- Create a Python file (with a `.py` extension) containing the code you want to reuse. This file becomes your module.

**Example: Creating a simple module with functions and variables:**

Create a file named `mymodule.py`:

```python
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

pi = 3.14159

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
```

**Importing Modules**

**Using import to include modules in a program:**
- Use the `import` statement to bring a module into your current script.

**Different ways to import:**
1. **Import the entire module:**
   ```python
   import mymodule
   ```

2. **Import specific attributes from a module:**
   ```python
   from mymodule import greet, pi, Circle
   ```

3. **Import a module with an alias:**
   ```python
   import mymodule as mm
   ```

**Using Imported Functions and Variables**

**Accessing and using functions and variables from imported modules:**

**Example with a custom module:**

```python
# main.py

# Import the entire module
import mymodule

print(mymodule.greet("Alice"))
print(f"Pi value: {mymodule.pi}")

circle = mymodule.Circle(5)
print(f"Area of circle: {circle.area()}")

# Import specific attributes
from mymodule import greet, pi, Circle

print(greet("Bob"))
print(f"Pi value: {pi}")

circle = Circle(7)
print(f"Area of circle: {circle.area()}")

# Import with an alias
import mymodule as mm

print(mm.greet("Charlie"))
print(f"Pi value: {mm.pi}")

circle = mm.Circle(10)
print(f"Area of circle: {circle.area()}")
```

**Built-in Modules**

**Overview of Python’s standard library:**
- Python comes with a rich standard library that includes many modules for various tasks, such as math operations, date and time manipulation, file handling, and more.

**Examples of commonly used built-in modules:**

1. **math module:**
   - Provides mathematical functions.
   - Example:
     ```python
     import math

     print(math.sqrt(16))  # Output: 4.0
     print(math.pi)  # Output: 3.141592653589793
     ```

2. **datetime module:**
   - Supplies classes for manipulating dates and times.
   - Example:
     ```python
     import datetime

     now = datetime.datetime.now()
     print(now)  # Output: current date and time

     today = datetime.date.today()
     print(today)  # Output: current date
     ```

3. **os module:**
   - Provides functions to interact with the operating system.
   - Example:
     ```python
     import os

     current_dir = os.getcwd()
     print(current_dir)  # Output: current working directory

     os.mkdir('new_directory')  # Create a new directory
     ```
