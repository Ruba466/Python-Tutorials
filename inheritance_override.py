# Parent class
class Animal:
    def speak(self):
        return "The animal makes a sound"

# Child class that inherits from Animal
class Dog(Animal):
    def speak(self):  # Overriding the speak method
        return "The dog barks"

# Another child class
class Cat(Animal):
    def speak(self):  # Overriding the speak method
        return "The cat meows"

# Create objects
a = Animal()
d = Dog()
c = Cat()

# Calling speak() method
print("Animal:", a.speak())
print("Dog:", d.speak())
print("Cat:", c.speak())
