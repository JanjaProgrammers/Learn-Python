
#### Packages

**Definition and Structure**

**What is a package?**
- A package is a way of organizing related modules into a directory hierarchy.
- A package is typically a directory containing a special `__init__.py` file (which can be empty) and one or more module files.

**Creating a Package**

**Directory structure of a package:**

```plaintext
mypackage/
    __init__.py
    module1.py
    module2.py
```

**Creating a package:**
- Create a directory with the desired package name.
- Add an `__init__.py` file to the directory.
- Add module files to the directory.

**Example:**

1. Create a directory named `mypackage`.
2. Inside `mypackage`, create an empty `__init__.py` file.
3. Add `module1.py`:

```python
# module1.py

def func1():
    return "Function 1 from module 1"
```

4. Add `module2.py`:

```python
# module2.py

def func2():
    return "Function 2 from module 2"
```

**Importing Packages**

**Importing from packages:**
- Use the `from ... import ...` syntax to import specific modules or functions from a package.

**Example:**

```python
# main.py

from mypackage import module1, module2

print(module1.func1())  # Output: Function 1 from module 1
print(module2.func2())  # Output: Function 2 from module 2

# Import specific functions
from mypackage.module1 import func1
from mypackage.module2 import func2

print(func1())  # Output: Function 1 from module 1
print(func2())  # Output: Function 2 from module 2
```

By understanding and utilizing modules and packages, you can keep your Python code organized, reusable, and maintainable.