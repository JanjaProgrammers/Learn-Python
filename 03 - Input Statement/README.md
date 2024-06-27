### Input

1. **Reading Input from the User:**

   - Use `input()` function to prompt the user for input.
   - Example:
     ```python
     name = input("Enter your name: ")
     ```
   - `input()` returns a string, which can be converted to other types as needed.

2. **Handling User Input:**

   - Input is typically stored as a string, so convert it to the desired type (int, float, etc.) using type casting.
   - Example:
     ```python
     age = int(input("Enter your age: "))
     ```

3. **Multiple Inputs:**
   - Use `split()` method to separate inputs entered in a single line.
   - Example:
     ```python
     numbers = input("Enter numbers separated by space: ").split()
     ```
   - Convert each item to the desired type if needed.
