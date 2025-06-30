# Shopping cart program

#item = input("What item would you like to buy?: ")
#price = float(input("What is the price?: "))
#quantity = int(input("How many would you like:"))
#total = price * quantity

#print(f"You have bought {quantity} x {price}/s")
#print(f"Your total is:{total}")

# Madlibs game

#adjective1 = input("Enter an adjective (description):")
#noun1 = input("Enter a noun (person, place, thing):")
#adjective2 = input("Enter an adjective (description):")
#verb = input("Enter a verb ending with 'ing':")
#adjective3 = input("Enter an adjective (description)")

#print(f"Today I went to a {adjective1} zoo.")
#print(f"In an exhibit, I saw a {noun1}")
#print(f"{noun1} was {adjective2} and {verb}")
#print(f"I feel {adjective3}")

# Python calculator

operator = input("Enter an operator ( + - * /) :")
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
print(result)
