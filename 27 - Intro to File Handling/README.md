# Introduction to File Handling
- **Importance of File Handling**
  - File handling is essential for reading and writing data to files.
  - Used in data storage, logging, configuration files, and more.
- **Types of Files**
  - **Text files**: Store data in plain text format (e.g., `.txt`, `.csv`).
  - **Binary files**: Store data in binary format (e.g., `.bin`, `.exe`).

## Opening and Closing Files
- **Opening Files**
  - Use the `open()` function to open a file.
  - Syntax: `file_object = open(filename, mode)`
  - **Modes**:
    - `'r'`: Read (default mode, file must exist).
    - `'w'`: Write (creates a new file or truncates an existing file).
    - `'a'`: Append (creates a new file if it doesn’t exist).
    - `'b'`: Binary mode (e.g., `'rb'`, `'wb'`).
    - `'r+'`: Read and write (file must exist).

  ```python
  # Examples:
  file = open('example.txt', 'r')  # Open for reading
  file = open('example.txt', 'w')  # Open for writing
  file = open('example.txt', 'a')  # Open for appending
  ```

- **Closing Files**
  - Always close a file after completing operations using `close()`.
  - Closing a file frees up system resources.

  ```python
  file.close()
  ```

- **Using `with` Statement**
  - Automatically closes the file after the block of code is executed.
  - More reliable and concise.

  ```python
  with open('example.txt', 'r') as file:
      data = file.read()
  ```

#### Reading Files
- **Reading the Entire File with `read()`**
  - Reads the entire content of the file as a single string.
  - Can specify the number of characters to read.

  ```python
  with open('example.txt', 'r') as file:
      content = file.read()
      print(content)
  ```

- **Reading Line by Line with `readline()`**
  - Reads one line at a time.
  - Useful for processing large files line by line.

  ```python
  with open('example.txt', 'r') as file:
      line = file.readline()
      while line:
          print(line, end='')
          line = file.readline()
  ```

- **Reading All Lines with `readlines()`**
  - Reads all lines into a list where each line is an element.

  ```python
  with open('example.txt', 'r') as file:
      lines = file.readlines()
      for line in lines:
          print(line, end='')
  ```

### Summary
- File handling is crucial for working with data stored in files.
- Python provides various modes for opening files (`'r'`, `'w'`, `'a'`, etc.).
- Always close files to free resources, preferably using the `with` statement.
- Methods for reading files include `read()`, `readline()`, and `readlines()`.