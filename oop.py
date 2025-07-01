# Working of car.py file
from car import Car

car1 = Car("Civic", 2025, "Black", False)
car2 = Car("Swift", 2024, "White", True)
car3 = Car("Cultus", 2023, "Silver", True)

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

car3.drive()
car2.stop()
car1.detail()
# END



# Class variables
class Student:

    class_year = 2025    #class variable
    num_student = 0

    def __init__(self, name, age):           # Constructor
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Ali", 20)
student2 = Student("Ahmed", 21)
#print(student1.name)
#print(student1.age)
#print(Student.class_year)
print(f"My graduating class of {Student.class_year} have {Student.num_student} students")
print(student1.name)
print(student2.name)



# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
cat.sleep()
mouse.eat()

mouse.speak()
cat.speak()
dog.speak()



# Multiple inheritance

class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass
class Fish(Prey, Predator):     # multiple inheritance
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

hawk.hunt()
fish.flee()