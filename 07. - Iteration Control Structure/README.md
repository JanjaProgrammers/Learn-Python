## Loops

### while Loop

- Repeats a block of code as long as a condition is true.

  ```python
  while condition:
      # code block
  ```

- **Example**:
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```

### for Loop

- Iterates over a sequence (such as a list, tuple, string) and executes a block of code for each item in the sequence.

  ```python
  for item in sequence:
      # code block
  ```

- **Example**:
  ```python
  fruits = ["apple", "banana", "cherry"]
  for fruit in fruits:
      print(fruit)
  ```

### Nested Loops

- Loops inside another loop.
  ```python
  for i in range(3):
      for j in range(2):
          print(f"i: {i}, j: {j}")
  ```

## Control Flow Statements

### break Statement

- Exits the loop immediately.

  ```python
  while condition:
      if some_condition:
          break
  ```

- **Example**:
  ```python
  for num in range(10):
      if num == 5:
          break
      print(num)
  ```

### continue Statement

- Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

  ```python
  while condition:
      if some_condition:
          continue
  ```

- **Example**:
  ```python
  for num in range(10):
      if num % 2 == 0:
          continue
      print(num)
  ```

### pass Statement

- Does nothing; it’s a placeholder for future code.

  ```python
  if condition:
      pass
  ```

- **Example**:
  ```python
  for num in range(5):
      if num == 3:
          pass
      else:
          print(num)
  ```
