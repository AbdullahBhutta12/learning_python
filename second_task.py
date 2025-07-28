import random
import os
import json

file_path = "results_2nd-task.json"
previous_data = {}
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        loaded = json.load(file) # previous_data = json.load(file)
        for key, value in loaded.items():
            if isinstance(value, dict) and "points" in value and "rounds" in value:
                previous_data[key] = value

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
                    inputs = input(": ")
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

    for name in persons:
        if name in previous_data:
            # previous_data[name]["points"] += persons[name]
            previous_data[name]["rounds"] += 1
        else:
            previous_data[name] = {
                "points": persons[name],
                "rounds": 1
            }

    with open(file_path, "w") as file:
        json.dump(previous_data, file, indent=4)

    print("Result:")
    for name in sorted(persons):
        if name in previous_data:
            points = persons[name]
            rounds = previous_data[name]["rounds"]
            total_average = points / rounds
            average = points / num_elements
            print(f"\n{name}:\n  Points = {points} \n  Present Average = {average:.2f} \n  Overall average = {total_average}  over  {rounds} round(s)")
        else:
            print(f"{name} No data found")

    print("\nData saved")

    print("Thanks")
else:
    print("Invalid input: Plz enter integer value only")