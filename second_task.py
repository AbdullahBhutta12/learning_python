import random
import os

dictionary = ["abdullah", "abrar", "adil", "ahmad", "ali", "arslan", "asim", "babar", "bahadur", "danial", "dawood", "faizan", "faiz", "hamid", "hashir", "hamza", "ibrahim", "iqbal", "ismail", "junaid", "kashif", "mahad", "majid", "muhamin", "muhammad", "muneeb", "muzamil", "nadeem", "noman", "omer", "qasim", "rashid", "rizwan", "sajid", "saleem", "salman", "saqib", "sharjeel", "talha", "umer", "usama", "usman", "waqas", "wasif", "younas", "zain"]

persons = []

num_elements = input("Enter the number of persons: ")

if num_elements.isdigit():
    num_elements = int(num_elements)
    for i in range(num_elements):
        while True:
            name = input(f"Enter person {i + 1} name: ")
            if name.lower() in dictionary:
                if name in persons:
                    print("This name is already taken. Please choose any other name next time")

                else:
                    persons.append(name)
                    break
            else:
                print(f"This name is not in dictionary. Please choose any name from this dictionary: {dictionary}")

    print(f"\nYou are {num_elements} persons {persons}")

    points = [0] * num_elements
    temp_persons = list(persons)

    for person in persons:

        while temp_persons:

            member = random.choice(temp_persons)
            print(f"\n{member}: Give (0-10) points to {persons}")

            for i in range(num_elements):
                while True:
                    print(persons[i])
                    inputs = input(":")
                    if inputs.isdigit():
                        inputs = int(inputs)
                        if 0 <= inputs <= 10:
                            points[i] = points[i] + inputs
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
