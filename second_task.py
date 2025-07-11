import random

persons = []
while True:
    num_elements = input("Enter the number of persons: ")

    print(type(num_elements))
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
                    inputs = int(input(":"))
                    points[i] = points[i] + inputs
                temp_persons.remove(member)

        x = 0
        print("\n\nResult:")
        while x < num_elements:
            print(f"Total points of {persons[x]} are {points[x]}")
            x += 1

        n = 0
        print("\nAverage:")
        while n < num_elements:
            average = points[n] / num_elements
            print(f"Average points of {persons[n]} are {average:1f}")
            n += 1

        print("\nThanks")
    else:
        print("Invalid input: Plz enter integer value only")