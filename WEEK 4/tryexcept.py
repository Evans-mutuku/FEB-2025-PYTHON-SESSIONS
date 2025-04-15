try:
    file = open("WEEK 4/example.txt", "r")
    data = file.read()
    print("The data is: ", data)
except FileNotFoundError:
    print("Sorry, This file does not exist")
finally:
    print("Thank you for using this program")
















# try:
#     with open("example.txt", "r") as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found. Please check the filename.")