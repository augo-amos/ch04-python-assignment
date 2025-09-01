# Python OOP & Control Flow Assignment

This repository contains solutions to assignments covering **Python Object-Oriented Programming (OOP)**, **Control Flow**, and **Functions**. The project is split into three Jupyter notebooks and one Python script, each focusing on a different concept.

---

## Files Included

1. **`classes_assignment.py`** – OOP (Classes, Objects & Methods)
2. **`control_flows_assignment.ipynb`** – Loops & Control Flow
3. **`functions_assignment.ipynb`** – Functions in Python

---

## 1. Classes Assignment (`classes_assignment.py`)

### **i. Student Class**

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  
    def display_info(self):
        print(f'Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}')
```

* Demonstrates class basics (attributes & methods).
* Three student objects were created and their details displayed.

---

### **ii. BankAccount Class with Class Method**

```python
class BankAccount:
    bank_name = "Equity Bank"   
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
```

* Includes `deposit()`, `withdraw()`, and `display_balance()`.
* Class method `display_bank_name()` shows use of `@classmethod`.

---

### **iii. Car Class (Encapsulation)**

```python
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0
```

* Private attributes (`__make`, `__model`, `__year`, `__speed`).
* Getter/setter methods for encapsulation.
* Methods to increase/decrease speed.

---

### **iv. Circle and Cylinder Classes (Objects as Arguments)**

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

class Cylinder:
    def __init__(self, circle, height):
        self.circle = circle
        self.height = height
    def volume(self):
        return self.circle.area() * self.height
```

* Demonstrates composition (using one object inside another).

---

### **v. Author and Book Classes (Aggregation)**

```python
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
```

* An `Author` object is shared across multiple `Book` objects.
* Demonstrates aggregation relationship.

---

### **vi. Rectangle Class (Challenge)**

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
```

* Methods `area()` and `perimeter()`.
* `compare_area()` compares areas between two rectangles.

---

## 2. Control Flows Assignment (`control_flows_assignment.ipynb`)

### **i. For Loop: Print 1–10**

```python
for i in range(1, 11):
    print(i)
```

### **ii. While Loop with Stop Condition**

```python
i = 1
while True:
    print(i)
    i += 1
    user_input = input("Type 'stop' to exit, or press enter to continue: ")
    if user_input.lower() == 'stop':
        break
```

### **Alternative with Threads**

```python
import threading, time
stop = False

def count_numbers():
    i = 1
    while not stop:
        print(i)
        i += 1
        time.sleep(0.5)

def wait_for_stop():
    global stop
    if input("Type 'stop' to end: ").lower() == "stop":
        stop = True
        print("Loop stopped by user.")
```

---

### **iii. Even Numbers 1–20**

```python
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```

Alternative with `while` loop also provided.

---

### **iv. Break and Continue (Explanation)**

* **Break** → exits a loop immediately, even if the condition is still true.
* **Continue** → skips the current iteration and moves to the next one.

---

### **v. Guessing Game (Challenge)**

```python
secret_number = 7

while True:
    guess = int(input("Type a number between 1 and 10: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number.")
        break
```

---

## 3. Functions Assignment (`functions_assignment.ipynb`)

This notebook demonstrates how to:

* Define functions
* Pass parameters
* Use return values
* Call functions from within other functions

Example:

```python
def greet(name):
    return f"Hello, {name}!"

def welcome_user(name):
    greeting = greet(name)
    print(greeting)
    print("Welcome to the program!")
```

---

## How to Run

1. Clone this repository.
2. Open Jupyter Notebook / JupyterLab.
3. Run each `.ipynb` file step by step.
4. Run `classes_assignment.py` as a Python script:

   ```bash
   python classes_assignment.py
   ```

---

## Summary

This project covers:

* **OOP**: Classes, Objects, Encapsulation, Aggregation, Class Methods
* **Control Flow**: For/While Loops, Break/Continue, User Interaction
* **Functions**: Reusable code blocks, calling functions inside others

Together, these exercises give a strong foundation in **Python programming**. 🚀
