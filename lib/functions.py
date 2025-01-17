#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("Sunny")  

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

def add(num1, num2):
    return num1 + num2

def halve(number):
    if isinstance(number, (int, float)):
        return number / 2
    else:
        return None

# Example usage
result = add(5, 3)
print("Sum:", result)

halved_value = halve(10)
print("Halved:", halved_value)
