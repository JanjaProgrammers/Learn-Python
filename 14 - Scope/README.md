#### Scope in Python

Scope refers to the region of a program where a variable is accessible. Python uses the LEGB rule to determine the scope of a variable, which stands for Local, Enclosing, Global, and Built-in scopes.

1. **Local Scope:**
   Variables defined within a function have a local scope and are only accessible within that function.

   **Example:**

   ```python
   def my_function():
       local_var = 10  # Local scope
       print(local_var)

   my_function()  # Output: 10
   # print(local_var)  # This would raise an error since local_var is not accessible here
   ```

2. **Enclosing Scope:**
   This is relevant in nested functions. A variable in an outer function is accessible to an inner function.

   **Example:**

   ```python
   def outer_function():
       outer_var = 20

       def inner_function():
           print(outer_var)  # Enclosing scope

       inner_function()

   outer_function()  # Output: 20
   ```

3. **Global Scope:**
   Variables defined at the top level of a script or module are in the global scope and are accessible from any function within the same module.

   **Example:**

   ```python
   global_var = 30  # Global scope

   def my_function():
       print(global_var)

   my_function()  # Output: 30
   ```

4. **Built-in Scope:**
   These are special reserved keywords in Python that are always available. Examples include `print`, `len`, etc.

   **Example:**

   ```python
   print(len("Hello"))  # Output: 5
   ```

#### Variables in Functions

1. **Local Variables:**
   Defined within a function and can only be used within that function.

   **Example:**

   ```python
   def add(a, b):
       result = a + b  # Local variable
       return result

   print(add(5, 3))  # Output: 8
   # print(result)  # This would raise an error since result is not accessible here
   ```

2. **Global Variables:**
   Defined outside of all functions and accessible throughout the entire module. Use the `global` keyword to modify a global variable inside a function.

   **Example:**

   ```python
   count = 0  # Global variable

   def increment():
       global count  # Declare the intention to use the global variable
       count += 1

   increment()
   print(count)  # Output: 1
   ```

3. **Nonlocal Variables:**
   Used in nested functions to refer to variables in the enclosing (non-global) scope. Use the `nonlocal` keyword to modify such variables.

   **Example:**

   ```python
   def outer_function():
       outer_var = 0

       def inner_function():
           nonlocal outer_var
           outer_var += 1
           print(outer_var)

       inner_function()
       inner_function()

   outer_function()  # Output: 1
                     #         2
   ```

### Best Practices:

- Use local variables whenever possible to avoid unintended side effects.
- Use global variables sparingly and with caution.
- Use descriptive variable names to improve code readability and maintainability.
- Keep variable scope as limited as possible to reduce the complexity of the code.
