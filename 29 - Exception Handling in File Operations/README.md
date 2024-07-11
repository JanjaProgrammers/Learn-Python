# Error Handling in File Operations

- **Using Try-Except Blocks**

  - Handle exceptions that may occur during file operations to ensure your program can recover gracefully.

  ```python
  try:
      with open('nonexistent_file.txt', 'r') as file:
          content = file.read()
  except FileNotFoundError:
      print("The file does not exist.")
  except IOError:
      print("An I/O error occurred.")
  ```

- **Common Exceptions**

  - `FileNotFoundError`: Raised when a file or directory is requested but doesn’t exist.
  - `IOError`: Raised when an I/O operation (such as a file operation) fails.

  ```python
  try:
      with open('example.txt', 'r') as file:
          content = file.read()
  except FileNotFoundError as fnf_error:
      print(fnf_error)
  except IOError as io_error:
      print(io_error)
  ```

- **Ensuring File Closure with Finally**

  - Use `finally` to ensure a file is closed, even if an exception occurs.

  ```python
  try:
      file = open('example.txt', 'r')
      content = file.read()
  except Exception as e:
      print(e)
  finally:
      file.close()
  ```
