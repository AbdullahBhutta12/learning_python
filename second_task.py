import random
import os

persons = {}

num_elements = input("Enter the number of persons: ")

if num_elements.isdigit():
    num_elements = int(num_elements)
    for i in range(num_elements):
        while True:
            name = input(f"Enter person {i + 1} name: ")
            if name.isalpha():
                name = name.lower()
                if name in persons:
                    print("This name is already taken.")
                else:
                    persons[name] = 0
                    break

            else:
                print("Warning: Only give string input.")

    print(f"\nYou are {num_elements} persons {persons}")

    temp_persons = list(persons.keys())
    persons_list = list(persons.keys())

    for person in persons:

        while temp_persons:

            member = random.choice(temp_persons)
            print(f"\n{member}: Give (0-10) points to {list(persons.keys())}")

            for i in range(num_elements):
                while True:
                    print(persons_list[i])
                    inputs = input(":")
                    if inputs.isdigit():
                        inputs = int(inputs)
                        if 0 <= inputs <= 10:
                            persons[persons_list[i]] += inputs
                            break
                        else:
                            print(
                                f"Invalid input: {inputs} considered as 0. You should have entered a number between (0-10).")
                    else:
                        print("Invalid input: Plz enter integer value only")

            temp_persons.remove(member)
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

    print("\nResult:")
    for name, point in persons.items():
        print(f"Total points of {name} are {point}")

    print("\nAverage:")
    for name, point in persons.items():
        average = point / num_elements
        print(f"Average points of {name} are {average:.2f}")
    #
    # file_path = "/home/abdullah-saeed/results_2nd-task.txt"
    # txt = "Results: \n"
    # with open(file_path, "w") as file:
    #     file.write(txt)

    print("\nThanks")
else:
    print("Invalid input: Plz enter integer value only")
