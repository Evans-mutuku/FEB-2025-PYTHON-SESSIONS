# class Car:
#     color = "red"
#     model = "BMW"

#     # Method/behaviour to display car details
#     def drive(self):
#         print("The car is driving")
#     def stop(self):
#         print("The car has stoped")
    
# my_car = Car()  # Create an instance of the Car class
# my_car.drive()  # Call the drive method
# my_car.stop() 
# print(my_car.color)  # Access the color attribute






# self is just like a pointer which refers to the instance of the class the method is in
# refers to the instance of the class and is used to access attributes and methods within the class.








# class Person:
#     # Constructor method to initialize the object
#     def __init__(self, name, age, height):
#         self.name = name  # Instance variable for name
#         self.age = age    # Instance variable for age
#         self.height = height

# personDetails = Person("John", 30, 54.5)  # Create an instance of the Person class

# print(personDetails.age)  # Access the name attribute









def add(x, y):
    return x + y
add(5, 10)




class jsDaddies_girlfriend:
    skin_color = "brownskin"
    age = 45
    height = 5.4
    name = "jsMammie"

    def jsMammi(self):
        print("jsMammie is a great cook")

class jsDaddies_G2(jsDaddies_girlfriend):
    pass

come_over = jsDaddies_girlfriend()
print(come_over.name)
come_over.jsMammi()












# example 2

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

my_car1 = Car("red", "BMW")
my_car2 = Car("white", "Volvo")
print(my_car1.color)  # Access the color attribute
print(my_car2.color)  # Access the color attribute