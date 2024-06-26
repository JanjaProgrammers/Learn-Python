
# Variables and Datatypes in Python

## Variables

- **Definition**: A variable is a named location used to store data in the memory.
- **Naming Rules**:
  - Must start with a letter (a-z, A-Z) or an underscore (_).
  - Followed by letters, digits (0-9), or underscores.
  - Case-sensitive (e.g., `myVar` and `myvar` are different variables).
  - Cannot be a reserved keyword (e.g., `for`, `while`, `class`, etc.).

- **Examples**:
  ```python
  x = 5
  name = "Alice"
  _age = 30
  ```

## Declaration and Initialization

- **Declaration**: In Python, variables do not need explicit declaration to reserve memory space. The declaration happens automatically when a value is assigned to a variable.
- **Initialization**: Assigning a value to a variable for the first time.

- **Syntax**:
  ```python
  variable_name = value
  ```

- **Examples**:
  ```python
  # Integer
  age = 25
  
  # Float
  temperature = 36.6
  
  # String
  name = "Alice"
  
  # List
  fruits = ["apple", "banana", "cherry"]
  
  # Tuple
  point = (10, 20)
  
  # Dictionary
  person = {"name": "Bob", "age": 30}
  
  # Set
  unique_numbers = {1, 2, 3}
  
  # Boolean
  is_student = True
  
  # NoneType
  result = None
  ```

## Multiple Assignments

- **Assigning the same value to multiple variables**:
  ```python
  a = b = c = 10
  ```

- **Assigning different values to multiple variables in one line**:
  ```python
  x, y, z = 1, 2.5, "Hello"
  ```

## Changing Variable Types

- Variables in Python are dynamic-typed, meaning you can change the type of a variable by reassigning it a different value.
  ```python
  var = 10   # var is an integer
  var = "Python"  # var is now a string
  ```

## Variable Scope

- **Global Variables**: Variables declared outside a function, available throughout the program.
  ```python
  global_var = "I am global"

  def foo():
      print(global_var)
  
  foo()  # Output: I am global
  ```

- **Local Variables**: Variables declared inside a function, available only within that function.
  ```python
  def bar():
      local_var = "I am local"
      print(local_var)
  
  bar()  # Output: I am local
  # print(local_var)  # Error: NameError: name 'local_var' is not defined
  ```

- **Global Keyword**: To modify a global variable inside a function.
  ```python
  global_var = "I am global"

  def baz():
      global global_var
      global_var = "Modified global"
  
  baz()
  print(global_var)  # Output: Modified global
  ```

## Datatypes

### Numeric Types
- **int**: Integer, whole numbers.
  ```python
  a = 10
  b = -5
  ```
- **float**: Floating-point number, decimal numbers.
  ```python
  pi = 3.14
  gravity = 9.81
  ```
- **complex**: Complex numbers.
  ```python
  z = 1 + 2j
  ```

### Sequence Types
- **str**: String, a sequence of characters.
  ```python
  greeting = "Hello, World!"
  ```
- **list**: Ordered, mutable collection of items.
  ```python
  fruits = ["apple", "banana", "cherry"]
  ```
- **tuple**: Ordered, immutable collection of items.
  ```python
  coordinates = (10, 20)
  ```

### Set Types
- **set**: Unordered collection of unique items.
  ```python
  unique_numbers = {1, 2, 3, 4, 5}
  ```

### Mapping Types
- **dict**: Collection of key-value pairs.
  ```python
  student = {"name": "John", "age": 21, "course": "Physics"}
  ```

### Boolean Type
- **bool**: Represents True or False.
  ```python
  is_student = True
  has_graduated = False
  ```

### None Type
- **NoneType**: Represents the absence of value or a null value.
  ```python
  result = None
  ```

## Type Conversion

- **Implicit Conversion**: Python automatically converts one data type to another.
  ```python
  x = 10   # int
  y = 3.14 # float
  z = x + y  # z becomes float (13.14)
  ```

- **Explicit Conversion**: Manually converting from one data type to another using type functions.
  ```python
  a = 5    # int
  b = "123" # str
  c = int(b)  # c becomes int (123)
  d = float(a)  # d becomes float (5.0)
  ```

## Checking Datatypes
- **Using `type()` function**: To check the datatype of a variable.
  ```python
  x = 10
  print(type(x))  # Output: <class 'int'>
  ```

## Best Practices

- Use meaningful variable names that convey the purpose of the variable.
- Follow the naming conventions (e.g., `snake_case` for variables).
- Avoid using Python reserved keywords as variable names.
