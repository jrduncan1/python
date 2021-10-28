class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"{self.first_name} {self.last_name} is walking {self.pet.name}!")
        return self

    def feed(self):
        self.pet.eat()
        print(f"{self.first_name} {self.last_name} is feeding {self.pet.name} {self.pet_food}!")
        return self

    def bathe(self):
        self.pet.noise()
        print(f"{self.first_name} {self.last_name} is bathing {self.pet.name}, and {self.pet.name} is NOT HAPPY!")
        return self

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0

    def sleep(self):
        self.health += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(f"{self.name} is barking at the Amazon delivery person, despite seeing them 3 times a week.")
        return self


chris = Ninja("Chris", "Farley", "fries", "burgers", Pet("Archer", "dog", "backflips"))

chris.feed()
chris.walk()
chris.bathe()
