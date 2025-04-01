temperature = 12

if temperature >= 20:
    print("It's a hot day")
elif temperature >= 10:
    print("It's a warm day")
elif temperature >= 0:
    print("It's a cold day")
else:
    print("It's a freezing day")


















# int


marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")  
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")