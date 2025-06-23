# Starting Python


# String
first_name = "Abdullah"
food = "Pizza"
email = "abdullah@gmail.com"
print(f"Hello{first_name}")
print(f"You like {food}")
print(f"Your email is {email}")
print(len(email))
print(email[10])

# Integers
age = 20
height = 5.6
print(f"You are {age} years old")
print(f"Your height is {height}")

# Escape sequences
course = "Python \"Programming\" "
message = "\nPython \nProgramming "
print(course, message)

# String
message = " This is a message"
print(len(message))
print(message[3])
print(message[-3])
print(message[0:5])
print(message[0:])
print(message[:9])

# Formatted string
first = "Abdullah"
last = "Saeed"
full = f"{first} {last} {2 * 2}"
print(full)

# String methods
course = "  Python programming "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("gram"))
print(course.replace("P", "J"))
print("gram" in course)
print("swift" not in course)

# Numbers
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 % 3)
print(10 ** 3)
print(10 // 3)

# Working with numbers

print(round(2.9))
print(abs(-31))
