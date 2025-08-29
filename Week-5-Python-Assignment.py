# Assignment 1: Smartphone Class

class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level  # percentage

    def call(self, contact):
        if self.battery_level > 0:
            print(f"Calling {contact} from {self.brand} {self.model}...")
            self.battery_level -= 5
        else:
            print(" Battery dead! Please charge.")

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f" Charged! Battery level is now {self.battery_level}%.")


# Inheritance Example: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_level, cooling_system):
        super().__init__(brand, model, battery_level)
        self.cooling_system = cooling_system  # e.g., "liquid cooling"

    # Polymorphism - override call()
    def call(self, contact):
        print(f" Gaming phone {self.brand} {self.model} is too busy playing games to call {contact}!")


# Create objects
phone1 = Smartphone("Apple", "iPhone 14", 80)
phone2 = GamingSmartphone("Asus", "ROG Phone 6", 50, "Liquid Cooling")

# Use methods
phone1.call("Alice")
phone1.charge(10)

phone2.call("Bob")
phone2.charge(30)


# Activity 2: Polymorphism with Animals

class Animal:
    def move(self):
        print("Animals can move in different ways.")

class Dog(Animal):
    def move(self):
        print(" Dog runs on four legs!")

class Bird(Animal):
    def move(self):
        print(" Bird flies in the sky!")

class Fish(Animal):
    def move(self):
        print(" Fish swims in water!")


# Test polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()