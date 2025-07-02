
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




# Multiple inheritance and multilevel inheritance

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):                                   # multilevel inheritance
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):                               # multilevel inheritance
    def hunt(self):
        print(f"{self.name} is hunting")

class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass
class Fish(Prey, Predator):                            # multiple inheritance
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

hawk.hunt()
fish.flee()
fish.eat()
rabbit.sleep()
