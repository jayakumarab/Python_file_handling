# Python File Handling – Complete Notes

## 1. Introduction

File Handling in Python is used to create, read, write, append, and manage files.

**Common file types:**
- Text files: `.txt`, `.csv`, `.json`
- Binary files: `.jpg`, `.png`, `.pdf`

## 2. Opening a File – `open()`

**Syntax:**
```python
file = open("filename.txt", "mode")
```

**Example:**
```python
file = open("student.txt", "r")
```

## 3. File Modes

| Mode | Description |
|---|---|
| `r` | Read an existing file |
| `w` | Write or overwrite file content |
| `a` | Append content at the end |
| `x` | Create a new file; error if it exists |

### Write Mode
```python
file = open("student.txt", "w")
file.write("Hello Python")
file.close()
```

### Append Mode
```python
file = open("student.txt", "a")
file.write("\nLearning Python")
file.close()
```

### Create Mode
```python
file = open("new.txt", "x")
file.close()
```

## 4. Reading Methods

### `read()`
Reads the complete file content.
```python
with open("student.txt", "r") as file:
    content = file.read()
    print(content)
```

### `readline()`
Reads one line at a time.
```python
with open("student.txt", "r") as file:
    line = file.readline()
    print(line)
```

### `readlines()`
Reads all lines and returns a list.
```python
with open("student.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

### Difference

| Method | Return Value |
|---|---|
| `read()` | String containing complete content |
| `readline()` | String containing one line |
| `readlines()` | List of strings |

## 5. Writing Methods

### `write()`
Writes a string into a file.
```python
with open("student.txt", "w") as file:
    file.write("Name: Jayakumar\n")
    file.write("Skill: Python\n")
```

### `writelines()`
Writes multiple strings from an iterable.
```python
details = [
    "Name: Jayakumar\n",
    "Skill: Python\n",
    "Goal: Full Stack Developer\n"
]

with open("student.txt", "w") as file:
    file.writelines(details)
```

**Note:** Neither `write()` nor `writelines()` automatically adds new lines. Use `\n` when required.

## 6. Closing a File – `close()`

Closes an opened file.
```python
file = open("student.txt", "r")
content = file.read()
print(content)
file.close()
```

## 7. Context Manager – `with open()`

Automatically closes the file after the block finishes.
```python
with open("student.txt", "r") as file:
    content = file.read()
    print(content)
```

**Best Practice:** Prefer `with open()` because it safely manages file closing, even when an exception occurs.

## 8. Exception Handling

Handles errors that may occur during file operations.
```python
try:
    with open("student.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found!")
```

| Keyword | Purpose |
|---|---|
| `try` | Executes code that may cause an error |
| `except` | Handles an exception |
| `else` | Runs if no exception occurs |
| `finally` | Runs whether an exception occurs or not |
| `raise` | Manually raises an exception |

## 9. Special Characters

| Character | Purpose |
|---|---|
| `\n` | New line |
| `\t` | Tab space |
| `\\` | Backslash |

## 10. Practical Project – Student Management System

**Project Features:**
- Add student details
- View all student details
- Search student by name
- Store information in a text file
- Handle missing file errors
- Display a menu using a `while` loop

**Technologies:** Python, File Handling, Functions, Loops, Conditions, Exception Handling.

## 11. Important Interview Questions

1. What is File Handling in Python?
2. What is the purpose of `open()`?
3. What are the different file modes?
4. What is the difference between `r`, `w`, and `a`?
5. What is the difference between `read()` and `readline()`?
6. What does `readlines()` return?
7. What is the difference between `write()` and `writelines()`?
8. Why do we use `close()`?
9. What is the advantage of `with open()`?
10. What is `FileNotFoundError`?

## 12. Learning Summary

- File creation and opening
- Reading and writing files
- File modes: `r`, `w`, `a`, `x`
- Reading methods: `read()`, `readline()`, `readlines()`
- Writing methods: `write()`, `writelines()`
- Closing files using `close()`
- Context managers using `with open()`
- Exception handling
- Student Management System project

---

