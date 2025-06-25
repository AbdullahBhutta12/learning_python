# for loop
for number in range(3):
    print("Attempt")

# for number in range(1,4):
#    print("Attempt", number, (number) * ".")

# for number in range(1,10,2):
#    print("Attempt", number, (number) * ".")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempt 3 times and failed")

# Nested loop
for x in range(1, 6):
    for y in range(1, 4):
        print(f"{x}, {y}")

# for x in range(1, 6):
#    for y in range(1, 4):
#        print(f"{x}, {y}")

for z in "Python":
    print(z)
