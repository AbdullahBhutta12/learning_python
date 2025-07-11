import random

persons = []

num_elements = int(input("Enter the number of persons: "))

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


# if 0 <= inputs >= 10:
            #
            # else:
            #     print("Plz give points between 0 to 10")