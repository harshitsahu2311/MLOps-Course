# Base Class
class Grandparent:
    def __init__(self, name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story.")

# Intermediate Class
class Parent(Grandparent):
    def work(self):
        print(f"{self.name} is working.")

# Derived Class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")

# Create instance of Child class
child = Child("Harshit")
child.tell_story()
child.work()
child.play()