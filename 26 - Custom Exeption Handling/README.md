# Custom Exceptions

Custom exceptions allow you to define your own error types to better reflect the specific issues that might arise in your application. This can make your error handling more precise and readable.


## Raising Exceptions
The `raise` keyword is used to manually trigger an exception. It is often used to create custom exceptions or to re-raise exceptions after catching them.

```python
if condition:
    raise ExceptionType("Custom error message")
```

**Example:**

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    age = check_age(-5)
except ValueError as e:
    print(f"Error: {e}")
```

## Define a custom exception class:**
   - Inherit from the built-in `Exception` class or a subclass of `Exception`.
   - Optionally, define an `__init__` method to customize initialization.

```python
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
```

2. **Example:**

```python
class InvalidAgeError(Exception):
    def __init__(self, age, message="Invalid age provided"):
        self.age = age
        self.message = message
        super().__init__(self.message)
```

**Raising and catching custom exceptions:**

1. **Raise the custom exception:**
   - Use the `raise` keyword to trigger the custom exception.

```python
def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return age
```

2. **Catch the custom exception:**
   - Use a `try-except` block to catch and handle the custom exception.

```python
try:
    age = check_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e.message} - Age provided: {e.age}")
```

#### Best Practices

**Using specific exceptions:**
- Always catch specific exceptions rather than using a general `except` block. This ensures you only handle expected errors and not unexpected ones that could mask bugs.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
```

**Avoiding bare except clauses:**
- Avoid using a bare `except:` clause, which catches all exceptions, including those you might not intend to handle (like `KeyboardInterrupt` or `SystemExit`).

```python
try:
    result = 10 / 0
except Exception as e:  # More specific than bare except
    print(f"An error occurred: {e}")
```

**Cleaning up resources with finally:**
- Use the `finally` block to ensure that cleanup code (such as closing files or releasing resources) is executed regardless of whether an exception occurred.

```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if file:
        file.close()
    print("File closed.")
```

By following these best practices, you can write more robust, maintainable, and predictable Python code, ensuring that your applications handle errors gracefully and effectively.