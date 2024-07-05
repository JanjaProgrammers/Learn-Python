class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):
    def eat(self):
        super().eat()
        print("The animal is a dog")

class DogChild(Dog):
    pass

dog = Dog()

dog.eat()
