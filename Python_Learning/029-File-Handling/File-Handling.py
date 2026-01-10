# Python File Handling

"""
This script demonstrates various aspects of file and directory handling in Python.
It covers:
- Basic file operations: opening, reading, writing, and appending.
- The importance of using the 'with' statement for automatic resource management.
- The 'os' module for interacting with the operating system, including:
  - File operations: renaming and deleting.
  - Directory operations: creating, listing, and removing.
- The 'os.path' module for platform-independent path manipulations.
- Additional file object methods.
"""

import os
import shutil

# Create a directory for file handling examples
if not os.path.exists("test_files"):
    os.makedirs("test_files")

# Change into the new directory to keep our project clean
os.chdir("test_files")

# --- 1. File Handling Introduction ---
print("--- 1. File Handling Introduction ---")
# File handling is a crucial part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# --- 2. The open() Function ---
print("\n--- 2. The open() Function ---")
# The key function for working with files in Python is the open() function.
# It takes two parameters; filename and mode.

# Modes for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
# "a" - Append - Opens a file for appending, creates the file if it does not exist.
# "w" - Write - Opens a file for writing, creates the file if it does not exist, overwrites existing content.
# "x" - Create - Creates the specified file, returns an error if the file exists.

# In addition, you can specify if the file should be handled in binary or text mode:
# "t" - Text - Default value. Text mode.
# "b" - Binary - Binary mode (e.g., for images).
# "+" - Read and Write

# --- 3. Writing to a File ---
print("\n--- 3. Writing to a File ---")
# It's best practice to use the 'with' statement, which handles closing the file automatically.

# Writing new content (overwrites existing file)
try:
    with open("example.txt", "w") as f:
        f.write("Hello, World!\n")
        f.write("This is the first line.\n")
        print("Successfully wrote to example.txt")
except IOError as e:
    print(f"Error writing to file: {e}")

# Appending content to an existing file
try:
    with open("example.txt", "a") as f:
        f.write("This line is appended.\n")
        print("Successfully appended to example.txt")
except IOError as e:
    print(f"Error appending to file: {e}")

# Writing multiple lines
lines_to_write = ["This is line one.\n", "This is line two.\n"]
try:
    with open("multiple_lines.txt", "w") as f:
        f.writelines(lines_to_write)
        print("Successfully wrote multiple lines to multiple_lines.txt")
except IOError as e:
    print(f"Error writing lines to file: {e}")

# --- 4. Reading from a File ---
print("\n--- 4. Reading from a File ---")

# Reading the entire file content
try:
    with open("example.txt", "r") as f:
        content = f.read()
        print("Reading entire file (example.txt):\n" + content)
except FileNotFoundError:
    print("Error: example.txt not found.")

# Reading a specific number of characters
try:
    with open("example.txt", "r") as f:
        content_part = f.read(12) # Reads the first 12 characters
        print(f"Reading first 12 characters: '{content_part}'")
except FileNotFoundError:
    print("Error: example.txt not found.")


# Reading line by line
print("\nReading file line by line (example.txt):")
try:
    with open("example.txt", "r") as f:
        line1 = f.readline()
        print("First line:", line1.strip())
        line2 = f.readline()
        print("Second line:", line2.strip())
except FileNotFoundError:
    print("Error: example.txt not found.")


# Reading all lines into a list
print("\nReading all lines into a list (multiple_lines.txt):")
try:
    with open("multiple_lines.txt", "r") as f:
        lines = f.readlines()
        print(lines)
except FileNotFoundError:
    print("Error: multiple_lines.txt not found.")


# Iterating over the file (the most memory-efficient way for large files)
print("\nIterating over the file (example.txt):")
try:
    with open("example.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Error: example.txt not found.")

# --- 5. File Renaming and Deleting ---
print("\n--- 5. File Renaming and Deleting ---")

# Renaming a file
try:
    os.rename("example.txt", "renamed_example.txt")
    print("File 'example.txt' was renamed to 'renamed_example.txt'")
except FileNotFoundError:
    print("Error: File to rename not found.")
except OSError as e:
    print(f"Error renaming file: {e}")

# Deleting a file
try:
    os.remove("renamed_example.txt")
    print("File 'renamed_example.txt' has been deleted.")
except FileNotFoundError:
    print("Error: File to delete not found.")
except OSError as e:
    print(f"Error deleting file: {e}")


# --- 6. Directory Management with 'os' Module ---
print("\n--- 6. Directory Management with 'os' Module ---")

# Get Current Working Directory
print(f"Current Working Directory: {os.getcwd()}")

# Create a directory
if not os.path.exists("my_new_directory"):
    os.mkdir("my_new_directory")
    print("Directory 'my_new_directory' created.")

# Create nested directories
if not os.path.exists("nested/dir/level3"):
    os.makedirs("nested/dir/level3")
    print("Nested directories 'nested/dir/level3' created.")

# List files and directories
print(f"Contents of current directory: {os.listdir('.')}")

# Remove a directory
try:
    os.rmdir("my_new_directory")
    print("Directory 'my_new_directory' removed.")
except OSError as e:
    print(f"Error removing directory: {e}")

# Remove nested directories
try:
    # shutil.rmtree is more powerful and can remove non-empty directories
    shutil.rmtree("nested")
    print("Directory tree 'nested' and its contents removed.")
except OSError as e:
    print(f"Error removing directory tree: {e}")


# --- 7. 'os.path' Module ---
print("\n--- 7. 'os.path' Module ---")

# Create a test file for path operations
with open("test_path.txt", "w") as f:
    f.write("Path test.")

file_path = "test_path.txt"
dir_path = "path_dir_test"
os.makedirs(dir_path, exist_ok=True)


# Join paths safely
# This is the recommended way to create file paths to ensure cross-platform compatibility.
full_path = os.path.join(os.getcwd(), file_path)
print(f"Joined Path: {full_path}")

# Check if path exists
print(f"Does '{file_path}' exist? {os.path.exists(file_path)}")
print(f"Does 'non_existent_file.txt' exist? {os.path.exists('non_existent_file.txt')}")

# Check if it's a file or directory
print(f"Is '{file_path}' a file? {os.path.isfile(file_path)}")
print(f"Is '{dir_path}' a file? {os.path.isfile(dir_path)}")
print(f"Is '{dir_path}' a directory? {os.path.isdir(dir_path)}")

# Get file size
print(f"Size of '{file_path}': {os.path.getsize(file_path)} bytes")

# Get directory name and base name
print(f"Directory Name: {os.path.dirname(full_path)}")
print(f"Base Name (file name): {os.path.basename(full_path)}")

# --- 8. Other File Methods ---
print("\n--- 8. Other File Methods ---")

with open("seek_example.txt", "w") as f:
    f.write("0123456789abcdefghijklmnopqrstuvwxyz")

with open("seek_example.txt", "r") as f:
    # Get the current file position
    print(f"Initial cursor position: {f.tell()}")

    # Move the cursor to the 10th byte (0-indexed)
    f.seek(10)
    print(f"Cursor position after seek(10): {f.tell()}")

    # Read from the new position
    print(f"Read after seeking: '{f.read(5)}'")
    print(f"Cursor position after reading 5 chars: {f.tell()}")

# Truncate a file
with open("seek_example.txt", "a+") as f:
    f.truncate(5) # Truncate the file to be 5 bytes long
    f.seek(0)
    print(f"\nContent of truncated file: '{f.read()}'")


# --- Cleanup ---
print("\n--- Cleanup ---")
# It's good practice to clean up created files and directories.
# Change back to the parent directory before deleting the 'test_files' directory
try:
    os.chdir("..")
    shutil.rmtree("test_files")
    print("Cleaned up the 'test_files' directory.")
except OSError as e:
    print(f"Error during cleanup: {e}")

print("\nFile handling script finished.")
