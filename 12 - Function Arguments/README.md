# Function Arguments

Function arguments are values passed to a function when it is called. These values are used as inputs to the function.

### Example:

**Function Definition:**

```python
def greet():
    print("Hello World!")
```

**Function Call:**

```python
greet()
```

Python supports several types of arguments:
1. **Default Parameters:**
   Default arguments are used to provide default values for parameters. If an argument is not provided, the default value is used.

   **Example:**

   ```python
   def greet(name="Dan"):
       print(f"Hello, {name}!")

   greet()  # Output: Hello, Dan!
   greet("Mary")  # Output: Hello, Mary!
   ```


2. **Keyword Arguments:**
   Keyword arguments are passed to a function by explicitly naming each parameter and assigning a value to it.

   **Example:**

   ```python
   def greet(name, message):
       print(f"{message}, {name}!")

   greet(name="Alice", message="Hello")
   ```
3. **Positional Arguments:**
   Positional arguments are the most common type of argument and are passed to a function in a specific order.

   **Example:**

   ```python
   def add(a, b):
       return a + b

   result = add(5, 3)
   print(result)  # Output: 8
   ```

4. **Variable-Length Arguments:**

   - **Arbitrary Positional Arguments (`*args`):** Used to pass a variable number of non-keyword arguments.
   - **Arbitrary Keyword Arguments (`**kwargs`):\*\* Used to pass a variable number of keyword arguments.

   **Example:**

   ```python
   def add_all(*args):
       return sum(args)

   print(add_all(1, 2, 3))  # Output: 6

   def print_details(**kwargs):
       for key, value in kwargs.items():
           print(f"{key}: {value}")

   print_details(name="Alice", age=30, city="New York")
   ```

**Best Practices:**

- Use descriptive names for function parameters.
- Provide default values for parameters when appropriate.
- Use `*args` and `**kwargs` for functions that need to handle a variable number of arguments.
- Document your functions with docstrings to explain the purpose of parameters and return values.
