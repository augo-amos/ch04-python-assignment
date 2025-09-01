'''
Assignment: Object-Oriented Programming (OOP) 
– Classes, Objects & Methods
Instructions:
Answer the following questions by defining appropriate classes, creating objects, and using methods.
Write clean, well-documented Python code for each question.
'''

# 1. Class and Object Basics
'''
Define a class named Student with the following attributes:
- name
- age
- grade
Create a method display_info() that prints the student's details.
Create three student objects and call the method for each to display their details.
'''
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  
    def display_info(self):
        print(f'Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}')

# Creating student objects
student1 = Student("Jack", 20, "A")
student2 = Student("Keith", 22, "B")
student3 = Student("Tony", 21, "A+")

# Displaying student information
student1.display_info()
student2.display_info()
student3.display_info() 

#2. Instance vs Class Methods

'''
Define a class named BankAccount with:
- account_number
- balance
Add methods:
- deposit(amount)
- withdraw(amount)
- display_balance()
Add a class variable to store the bank name and a class method to display the bank name.
Create two account objects and perform deposits and withdrawals.
'''
class BankAccount:
    bank_name = "Equity Bank"   
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited: {amount}. New Balance: {self.balance}')  

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew: {amount}. New Balance: {self.balance}')
        else:
            print('Insufficient funds')

    def display_balance(self):
        print(f'Account Number: {self.account_number}, Balance: {self.balance}')

    @classmethod
    def display_bank_name(cls):
        print(f'Bank Name: {cls.bank_name}')

# Creating bank account objects
account1 = BankAccount("123456")
account2 = BankAccount("654321", 500)

# Performing transactions
account1.deposit(200)
account1.withdraw(50)
account1.display_balance()

account2.deposit(300)
account2.withdraw(1000)  
account2.display_balance()

# Displaying bank name using class method
BankAccount.display_bank_name()


#3. Encapsulation
'''
Create a class Car with:
Private attributes: __make, __model, __year, __speed
Methods to:
Get and set make, model, and year.
Increase and decrease speed.
Display all car details.
Create a Car object, update its attributes, and demonstrate encapsulation.
'''
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0
    def get_make(self):
        return self.__make
    
    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model
    
    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        self.__year = year

    def increase_speed(self, increment):
        self.__speed += increment
        print(f'Speed increased by {increment}. Current speed: {self.__speed} km/h')

    def decrease_speed(self, decrement):
        if decrement <= self.__speed:
            self.__speed -= decrement
            print(f'Speed decreased by {decrement}. Current speed: {self.__speed} km/h')
        else:
            print('Speed cannot be negative')

    def display_details(self):
        print(f'Car Make: {self.__make}, Model: {self.__model}, Year: {self.__year}, Speed: {self.__speed} km/h')

# Creating a Car object
my_car = Car("Toyota", "Corolla", 2020)

# Updating attributes
my_car.set_make("Honda")
my_car.set_model("Civic")
my_car.set_year(2021)   

# Demonstrating encapsulation
my_car.increase_speed(50)
my_car.decrease_speed(20)
my_car.display_details()

#4. Methods with Objects as Arguments
'''
Create a class Circle with:
Attributes: radius
Method area() and circumference().
Create a class Cylinder that takes a Circle object and height.
Method volume() to compute the volume using the circle's area.
Demonstrate by creating a Circle object and passing it to the Cylinder object.
'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def circumference(self):
        return 2 * math.pi * self.radius
class Cylinder:
    def __init__(self, circle, height):
        self.circle = circle
        self.height = height
    def volume(self):
        return self.circle.area() * self.height
                                                                                                                                                                                                                
# Creating a Circle object
my_circle = Circle(5)

# Creating a Cylinder object using the Circle object
my_cylinder = Cylinder(my_circle, 10)

# Displaying area, circumference, and volume
print(f'Circle Area: {my_circle.area()}')
print(f'Circle Circumference: {my_circle.circumference()}')
print(f'Cylinder Volume: {my_cylinder.volume()}')   


#5. Object Relationships (Aggregation)
'''
Create a class Author with:
Attributes: name, nationality
Method to display author info.
Create a class Book with:
Attributes: title, price, and author (Author object).
Method to display book details including author info.
Create one author and multiple books related to that author.
'''
class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def display_info(self):
        print(f"Author: {self.name}, Nationality: {self.nationality}")


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author   # Author object

    def display_details(self):
        print(f"Book Title: {self.title}, Price: ${self.price}")
        self.author.display_info()  # Call Author's method inside Book


# Create an Author object
author1 = Author("John Maxwell", "American")

# Create multiple Book objects linked to the same author
book1 = Book("Leadership Gold", 15.99, author1)
book2 = Book("Today Matters", 12.50, author1)
book3 = Book("Intentional Living", 14.75, author1)

# Display book details
book1.display_details()
book2.display_details()
book3.display_details()

#6. Assignment Challenge (Optional)

'''
Create a class Rectangle with:
Attributes: length and width
Method area() and perimeter().
Write a method that takes another rectangle object as an argument and compares their areas.
Create multiple rectangles and compare them.
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def compare_area(self, other_rectangle):
        if self.area() > other_rectangle.area():
            return f'This rectangle has a larger area.'
        elif self.area() < other_rectangle.area():
            return f'The other rectangle has a larger area.'
        else:
            return 'Both rectangles have the same area.'
        
# Creating multiple Rectangle objects
rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 6)
rect3 = Rectangle(4, 5) 

# Comparing rectangles
print(f'Rectangle 1 Area: {rect1.area()}')
print(f'Rectangle 2 Area: {rect2.area()}')
print(rect1.compare_area(rect2))  

print(f'Rectangle 1 Area: {rect1.area()}')
print(f'Rectangle 3 Area: {rect3.area()}')
print(rect1.compare_area(rect3))

print(f'Rectangle 2 Area: {rect2.area()}')
print(f'Rectangle 3 Area: {rect3.area()}')
print(rect2.compare_area(rect3))    
