try:
    file = open("automata.docx", "r")
    data = file.read()
    print("The data is: ", data)
except UnicodeDecodeError:
    print("Sorry, This is a wrong format")
finally:
    print("This is the finally block")
















# try:
#     with open("example.txt", "r") as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found. Please check the filename.")