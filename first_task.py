

evens = []
odds = []

print("Enter any numbers(enter 'q' for exit.)")

while True:

    user = input("Number:")
    if user.lower() == 'q':
        break

    if user.isdigit():
        number = int(user)
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    else:
        print("Only enter integers or 'q'")

total_num = evens + odds

print("Total numbers entered:", len(total_num))
print("You have enter given even numbers:", evens)
print("You have enter given odd numbers:", odds)

