# Single Inheritance

# Base Class
class Parent:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Derived Class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of Child
child = Child("Harshit")
child.greet()
child.play()