# for loop


# for number in range(3):
#    print("Attempt")

# for number in range(1,4):
#    print("Attempt", number, (number) * ".")

# for number in range(1,10,2):
#    print("Attempt", number, (number) * ".")

#successful = False
#for number in range(3):
#    print("Attempt")
#    if successful:
#        print("Successful")
#        break
#else:
#    print("Attempt 3 times and failed")



# Nested loop

#for x in range(1, 6):
#    for y in range(1, 4):
#        print(f"{x}, {y}")

# for x in range(1, 6):
#    for y in range(1, 4):
#        print(f"{x}, {y}")

# for z in "Python":
#    print(z)



# while loop

#number = 100
#while number > 0:
#    print(number)
#    number //= 2

# command = ""
# while command != "quit" and command != "Quit":
#    command = input(">")
#    print("ECHO", command)

# command = ""
# while command.lower() != "quit":
#    command = input(">")
#    print("ECHO", command)



# Infinite loop

# command = ""
# while True:
#    command = input(">")
#    print("ECHO", command)
#    if command.lower() == "quit":
#        break

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")


