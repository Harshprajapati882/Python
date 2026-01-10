# Python File and Directory Handling

This document provides a comprehensive overview of file and directory handling in Python, covering the built-in `open` function, and the powerful `os` and `shutil` modules.

---

## 1. File Handling Basics

File handling is the process of working with files on the disk. This includes creating, reading, updating, and deleting files.

### The `open()` Function

The core function for file operations is `open()`.

**Syntax:** `open(filename, mode)`

-   `filename`: The path to the file.
-   `mode`: A string indicating how the file should be opened.

### File Modes

The most common modes are:

-   `'r'`: **Read** (default). Opens a file for reading. Raises an error if the file does not exist.
-   `'w'`: **Write**. Opens a file for writing. Creates the file if it does not exist. **Overwrites** the entire file if it exists.
-   `'a'`: **Append**. Opens a file for appending new content to the end. Creates the file if it does not exist.
-   `'x'`: **Create**. Creates a new file. Raises an error if the file already exists.

You can also specify the file handling mode:

-   `'t'`: **Text** (default). The file is handled as a text file.
-   `'b'`: **Binary**. The file is handled in binary mode (e.g., for images, audio).

You can combine modes, for example, `'+'` for read and write access:

-   `'r+'`: Read and write. The file pointer is at the beginning.
-   `'w+'`: Write and read. Overwrites the existing file or creates a new one.
-   `'a+'`: Append and read. The file pointer is at the end of the file if it exists.

### Using `with open(...)`

The recommended way to open a file is using the `with` statement. It automatically closes the file when the block is exited, even if errors occur.

```python
# Good Practice
with open('example.txt', 'w') as f:
    f.write('Hello, Python!')

# Bad Practice (requires manual closing)
# f = open('example.txt', 'w')
# f.write('Hello, Python!')
# f.close()
```

---

## 2. Writing to Files

### `write()`

Writes a single string to the file.

```python
with open('data.txt', 'w') as f:
    f.write('First line.\n')
    f.write('Second line.\n')
```

### `writelines()`

Writes a list of strings to the file. Note that it does not add newline characters automatically.

```python
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('data.txt', 'w') as f:
    f.writelines(lines)
```

---

## 3. Reading from Files

### `read()`

Reads the entire content of the file into a single string. You can also specify the number of characters to read.

```python
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)

with open('data.txt', 'r') as f:
    # Reads the first 10 characters
    first_10_chars = f.read(10)
    print(first_10_chars)
```

### `readline()`

Reads a single line from the file, including the newline character `\n`.

```python
with open('data.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1.strip()) # .strip() removes leading/trailing whitespace
```

### `readlines()`

Reads all lines from the file and returns them as a list of strings.

```python
with open('data.txt', 'r') as f:
    all_lines = f.readlines()
    print(all_lines)
```

### Iterating Over a File

This is the most memory-efficient way to read a large file line by line.

```python
with open('large_file.txt', 'r') as f:
    for line in f:
        print(line, end='')
```

---

## 4. File Object Methods

File objects have other useful methods:

-   `seek(offset)`: Moves the file cursor to a specific byte position.
-   `tell()`: Returns the current byte position of the cursor.
-   `truncate(size)`: Resizes the file to a specified size in bytes.

```python
with open('test.txt', 'w') as f:
    f.write('0123456789')

with open('test.txt', 'r+') as f:
    f.seek(5)         # Move to the 6th byte
    print(f.read(2))  # Reads '56'
    print(f.tell())   # Prints 7
    f.truncate(3)     # Truncates the file to 3 bytes long
    f.seek(0)
    print(f.read())   # Prints '012'
```

---

## 5. The `os` Module: File and Directory Operations

The `os` module provides a way of using operating system-dependent functionality.

### File Operations

-   `os.rename(src, dst)`: Renames a file or directory from `src` to `dst`.
-   `os.remove(path)`: Deletes a file at the given `path`.

```python
import os

# Create a dummy file
with open('to_delete.txt', 'w') as f:
    f.write('temp')

# Rename it
os.rename('to_delete.txt', 'renamed.txt')

# Delete it
os.remove('renamed.txt')
```

### Directory Operations

-   `os.getcwd()`: Gets the current working directory.
-   `os.chdir(path)`: Changes the current working directory.
-   `os.listdir(path)`: Returns a list of all files and directories in a given directory.
-   `os.mkdir(path)`: Creates a single directory. Fails if the directory already exists.
-   `os.makedirs(path)`: Creates directories recursively. Can be set to not fail if they exist (`exist_ok=True`).
-   `os.rmdir(path)`: Removes an **empty** directory.
-   `os.removedirs(path)`: Removes directories recursively.

```python
import os

print('Current Directory:', os.getcwd())

# Create directory
if not os.path.exists('my_folder'):
    os.mkdir('my_folder')

print('Directory Contents:', os.listdir('.'))

# Remove directory
os.rmdir('my_folder')
```

### The `shutil` Module for Advanced Operations

For more powerful directory operations, use the `shutil` module.

-   `shutil.rmtree(path)`: Deletes a directory and all its contents (files and subdirectories). **Use with caution!**

```python
import shutil
import os

os.makedirs('nested/dir', exist_ok=True)
with open('nested/dir/file.txt', 'w') as f:
    f.write('hello')

# This would fail: os.rmdir('nested')

# This will succeed
shutil.rmtree('nested')
```

---

## 6. The `os.path` Module

The `os.path` module is essential for manipulating file paths in a way that is compatible across different operating systems (Windows, macOS, Linux).

-   `os.path.join(path, *paths)`: Joins path components intelligently. This is the correct way to build paths.
-   `os.path.exists(path)`: Returns `True` if the path exists (both files and directories).
-   `os.path.isfile(path)`: Returns `True` if the path is an existing regular file.
-   `os.path.isdir(path)`: Returns `True` if the path is an existing directory.
-   `os.path.getsize(path)`: Returns the size of a file in bytes.
-   `os.path.basename(path)`: Returns the final component of a path (the file or directory name).
-   `os.path.dirname(path)`: Returns the directory part of a path.

```python
import os

# Create a platform-independent path
file_path = os.path.join('my_dir', 'data', 'file.txt')
print(file_path) # Output: my_dir/data/file.txt (on Linux/macOS)
                 # Output: my_dir\\data\\file.txt (on Windows)

# Check path properties
print('Exists:', os.path.exists(file_path))
print('Is File:', os.path.isfile(file_path))
print('Directory:', os.path.dirname(file_path))
print('Basename:', os.path.basename(file_path))
```
