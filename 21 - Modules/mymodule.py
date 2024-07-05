def greet(name):
    return f"Hello, {name}!"

pi = 3.14159

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)