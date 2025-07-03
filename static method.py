

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position} "

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


employee1 = Employee("Ali", "Manager")
employee2 = Employee("Adnan", "Cashier")
employee3 = Employee("Zafar", "Cook")


print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Security Guard"))
print(Employee.is_valid_position("Cashier"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())