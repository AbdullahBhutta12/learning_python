# 1.file detection

# import os

# file_path = "/home/abdullah-saeed/Downloads/Kotlin_Course_Contents.docx"        # absolute file path
# file_path = "stuff/file_detection.txt"                                            # relative file path
# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")
#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist")



# -----------------------------------------------------
# 2.writing files (.txt, .json, .csv)


# .txt

# employees = ["abdullah", "abrar", "adil", "ahmad", "ali", "arslan"]
# txt_data = "I like sandwich"
# file_path = "/home/abdullah-saeed/output.txt"
# try:
#     with open(file_path, "w") as file:
#     # with open(file_path, "a") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("This file already exist!")


# txt = "Hello ab!"
# file_path1 = "/home/abdullah-saeed/ab.txt"
# try:
#     with open(file_path1, "w") as file:
#         file.write(txt)
#         print(f"txt file '{file_path1}' is created")
# except FileExistsError:
#     print("This file already exist")



# .json

# import json
#
# employee = {
#     "name": "Ali",
#     "age": 20,
#     "job": "accountant"
# }
# file_path = "/home/abdullah-saeed/output.json"
# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("This file already exist!")



# .csv

# import csv
#
# employee = [["Name", "Age", "Job"],
#             ["Babar", 40, "Manager"],
#             ["Kashif", 30, "Accountant"],
#             ["Ibrahim", 25, "Account manager"]]
# file_path = "/home/abdullah-saeed/output.csv"
# try:
#     with open(file_path, "w") as file:
#         writer = csv.writer(file)
#         for row in employee:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("This file already exist!")




# ---------------------------------------------
# 3.reading files(.txt, .json, .csv)


# .txt

# file_path = "/home/abdullah-saeed/output.txt"
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")


# .json

# import json
# file_path = "/home/abdullah-saeed/output.json"
# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         # print(content["name"])
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")


# .csv

import csv
file_path = "/home/abdullah-saeed/output.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            # print(line[0])
except FileNotFoundError:
    print("That file was not found")