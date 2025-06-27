# Functions

#def show():
#    print("This is a user define function")

#show()


# Parameters and Arguments

def function(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("This is a user define function")

function("Abdullah", "Saeed")


def greet(name):
    return f"Hi {name}"
message = greet("Ali")
print(message)


#def add(num1, num2 = 1):
#    return num1 + num2
#print(add(4,5))
#print(add(9))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))