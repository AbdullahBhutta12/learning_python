
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")
    def detail(self):
        print(f"{self.year} {self.color} {self.model}")



class Auto(Car):
    pass

class Manual(Car):
    pass

class Civic(Auto):
    pass

class Corolla(Manual, Auto):
    pass

class Yaris(Manual, Auto):
    pass

class Mehran(Manual):
    pass
