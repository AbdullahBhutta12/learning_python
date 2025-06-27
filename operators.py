# Conditional statements

temperature = 26
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature >= 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


# Ternary Operator

age = 16
# if age >= 18:
#    message = "Eligible"
# else:
#   message = "Not eligible"
#   print(message)
message = "Eligible" if age >= 18 else "Not eligible"
print(message)


# Logical Operators

high_income = False
good_credit = True
student = False

# if high_income and good_credit:                      #and
# if high_income or good_credit:                       #or
# if not student:                                      #not
if (high_income or good_credit) and not student:  # complex
    print("Eligible")
else:
    print("Not eligible")

# Chaining comparison operators
# rule: Age should be between 18 and 60

age = 22
#if age >= 18 and age < 60:
if 18 <= age < 60:
   print("Welcome")
