

even_numbers = []
odd_numbers = []

print("Enter any numbers(enter 'q' for exit.)")

while True:

    user = input("Number:")
    if user.lower() == 'q':
        break

    if user.isdigit():
        number = int(user)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    else:
        print("Only enter integers or 'q'")

total_num = even_numbers + odd_numbers

print("Total numbers entered:", len(total_num))
print(f"You have enter {even_numbers} even numbers:")
print(f"You have enter {odd_numbers} odd numbers:")

