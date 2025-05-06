class SecretStash:
    def __init__(self):
        self.__chocolates = 10  # Private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left 😢")

stash = SecretStash()
stash.take_chocolate()

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def fight_crime(self):
        print(f"{self.name} uses {self.power} to fight crime in {self.city}!")

hero1 = Superhero("BoltMan", "Electric Shock", "Volt City")
hero1.fight_crime()