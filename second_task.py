import random
import os

persons = []

num_elements = input("Enter the number of persons: ")

if num_elements.isdigit():
    num_elements = int(num_elements)
    for i in range(num_elements):
        element = input(f"Enter person {i + 1} name: ")
        persons.append(element)

    print(f"\nYou are {num_elements} persons {persons}")

    points = [0] * num_elements
    temp_persons = list(persons)

    for person in persons:

        while temp_persons:

            member = random.choice(temp_persons)
            print(f"\n{member}: Give (0-10) points to {persons}")

            for i in range(num_elements):
                print(persons[i])
                inputs = input(":")
                if inputs.isdigit():
                    inputs = int(inputs)
                    if 0 <= inputs <= 10:
                        points[i] = points[i] + inputs
                    else:
                        print("Invalid input: Plz enter integer between (0-10).")
            temp_persons.remove(member)
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

    x = 0
    print("\nResult:")
    while x < num_elements:
        print(f"Total points of {persons[x]} are {points[x]}")
        x += 1

    n = 0
    print("\nAverage:")
    while n < num_elements:
        average = points[n] / num_elements
        print(f"Average points of {persons[n]} are {average:.2f}")
        n += 1

    print("\nThanks")
else:
    print("Invalid input: Plz enter integer value only")

#
# dictionary: dict = {"A" : ["Abdullah", "Adil", "Ahmad", "Ali"]
#               , "B" : ["Babar", "Bahadur"]
#               , "D" : ["Danial", "Dawood"]
#               , "H" : ["Hamid", "Hashir"]}
#
# import sys
# print(dictionary)
# print("Hamid" in dictionary)
#
# if inputs.isdigit():
#     inputs = int(inputs)
#     points[i] = points[i] + inputs
# else:
#     print("Invalid input: Plz enter integer value only\n END")
#     sys.exit()
