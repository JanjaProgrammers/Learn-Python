# File Handling Techniques

- **`os` Module**: Provides a way to interact with the operating system, including file path manipulations.

  ```python
  import os

  # Get current working directory
  cwd = os.getcwd()
  print(cwd)
  ```

## File Operations

- **Renaming a File**

  ```python
  import os

  os.rename('old_name.txt', 'new_name.txt')
  ```

- **Deleting a File**

  ```python
  import os

  os.remove('example.txt')
  ```

- **Checking if a File Exists**

  ```python
  import os

  if os.path.exists('example.txt'):
      print("File exists.")
  else:
      print("File does not exist.")
  ```
