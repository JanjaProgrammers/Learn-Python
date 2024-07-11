# Writing to Files

- **Writing a String with `write()`**

  - Writes a single string to a file.
  - File modes: `'w'` (write) and `'a'` (append).
  - Using `'w'` mode will overwrite the file if it exists.
  - Using `'a'` mode will append to the end of the file if it exists.

  ```python
  # Writing a single string to a file
  with open('example.txt', 'w') as file:
      file.write("Hello, World!\n")
  ```

- **Writing Multiple Lines with `writelines()`**

  - Writes a list of strings to a file.
  - Each element of the list should be a string.

  ```python
  # Writing multiple lines to a file
  lines = ["First line.\n", "Second line.\n", "Third line.\n"]
  with open('example.txt', 'w') as file:
      file.writelines(lines)
  ```

- **File Modes: `'w'` vs `'a'`**

  - `'w'`: Write mode. Creates a new file or truncates an existing file.
  - `'a'`: Append mode. Creates a new file if it doesn’t exist and appends to the end of the file.

  - **`'x'`: Create mode. Creates a file, returns an error if the file exist**

  ```python
  # Appending to a file
  with open('example.txt', 'a') as file:
      file.write("Appending a new line.\n")
  ```

### Summary

- Writing to files is done using `write()` and `writelines()`.
- File modes `'w'` and `'a'` are used for writing and appending, respectively.
- Binary files store data in a binary format and are handled using `'b'` mode.
- Practice writing and reading both text and binary files to reinforce learning.
