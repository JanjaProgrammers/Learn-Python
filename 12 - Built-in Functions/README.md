### Built-in Functions in Python

Python provides a rich set of built-in functions that are always available and do not require any import statement. These functions perform a wide variety of tasks, such as data type conversions, mathematical operations, and input/output operations. Here are some of the most commonly used built-in functions in Python:

#### 1. **Data Type Conversion Functions**
These functions are used to convert data from one type to another.

- `int()`: Converts a value to an integer.
  ```python
  num = int("10")
  print(num)  # Output: 10
  ```

- `float()`: Converts a value to a floating-point number.
  ```python
  num = float("10.5")
  print(num)  # Output: 10.5
  ```

- `str()`: Converts a value to a string.
  ```python
  num_str = str(10)
  print(num_str)  # Output: '10'
  ```

- `bool()`: Converts a value to a boolean.
  ```python
  val = bool(1)
  print(val)  # Output: True
  ```

#### 2. **Mathematical Functions**
These functions perform mathematical operations.

- `abs()`: Returns the absolute value of a number.
  ```python
  result = abs(-5)
  print(result)  # Output: 5
  ```

- `round()`: Rounds a number to a given precision in decimal digits.
  ```python
  result = round(3.14159, 2)
  print(result)  # Output: 3.14
  ```

- `max()`: Returns the largest item in an iterable or the largest of two or more arguments.
  ```python
  result = max(1, 5, 3)
  print(result)  # Output: 5
  ```

- `min()`: Returns the smallest item in an iterable or the smallest of two or more arguments.
  ```python
  result = min(1, 5, 3)
  print(result)  # Output: 1
  ```

- `sum()`: Sums the items of an iterable.
  ```python
  result = sum([1, 2, 3, 4])
  print(result)  # Output: 10
  ```

#### 3. **Sequence Functions**
These functions operate on sequences like lists, tuples, and strings.

- `len()`: Returns the number of items in an object.
  ```python
  length = len([1, 2, 3])
  print(length)  # Output: 3
  ```

- `sorted()`: Returns a sorted list from the items in an iterable.
  ```python
  sorted_list = sorted([3, 1, 2])
  print(sorted_list)  # Output: [1, 2, 3]
  ```

- `reversed()`: Returns a reversed iterator.
  ```python
  rev = list(reversed([1, 2, 3]))
  print(rev)  # Output: [3, 2, 1]
  ```

- `enumerate()`: Returns an enumerate object.
  ```python
  for index, value in enumerate(['a', 'b', 'c']):
      print(index, value)
  # Output: 0 a
  #         1 b
  #         2 c
  ```

#### 4. **Input/Output Functions**
These functions handle input and output operations.

- `print()`: Prints the specified message to the console.
  ```python
  print("Hello, World!")
  # Output: Hello, World!
  ```

- `input()`: Reads a line from input, converts it to a string.
  ```python
  name = input("Enter your name: ")
  print(f"Hello, {name}!")
  ```

#### 5. **Type Checking Functions**
These functions check the type of an object.

- `type()`: Returns the type of an object.
  ```python
  print(type(10))  # Output: <class 'int'>
  ```

- `isinstance()`: Checks if an object is an instance of a class or a tuple of classes.
  ```python
  print(isinstance(10, int))  # Output: True
  ```

#### 6. **Utility Functions**
These functions perform various utility tasks.

- `range()`: Generates a sequence of numbers.
  ```python
  for i in range(5):
      print(i)
  # Output: 0 1 2 3 4
  ```

- `zip()`: Aggregates elements from two or more iterables.
  ```python
  names = ['Alice', 'Bob']
  scores = [85, 92]
  paired = list(zip(names, scores))
  print(paired)  # Output: [('Alice', 85), ('Bob', 92)]
  ```

- `any()`: Returns `True` if any element of an iterable is true.
  ```python
  result = any([False, True, False])
  print(result)  # Output: True
  ```

- `all()`: Returns `True` if all elements of an iterable are true.
  ```python
  result = all([True, True, True])
  print(result)  # Output: True
  ```

These are just a few examples of Python's built-in functions. They provide powerful capabilities and help make Python a highly versatile and efficient programming language.
