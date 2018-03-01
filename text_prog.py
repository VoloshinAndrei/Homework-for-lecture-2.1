class DomesticAnimals:
    weight = 10  # kg
    height = 50  # cm
    favorite_food = None
    animal_name = None
    animal_group = None

    def __init__(self, animal_group, animal_name, favorite_food, height, weight):
        self.animal_group = animal_group
        self.animal_name = animal_name
        self.favorite_food = favorite_food
        self.height = height
        self.weight = weight

    def eat(self, value):
        self.weight += value


class LargeAnimal(DomesticAnimals):
    def give_meat(self):
        print("You have meat", self.animal_group, " - ", self.weight, " kg")
        self.weight = 0


class BirdAnimal(DomesticAnimals):
    def give_feather(self):
        print("You have feather", self.animal_group)
        self.weight -= 1


x1 = LargeAnimal("cows", "Буренка", "Сено", 100, 500)
# print(x1.weight)
x1.give_meat()
# print(x1.weight)

x2 = LargeAnimal("goats", "Буренка", "Сено", 100, 500)
print(x2.animal_group)
x2.animal_group = "cows"
print(x2.animal_group)

y1 = BirdAnimal("duck", "ГуГу", "трава", 40, 20)
# print(y1.weight)
y1.give_feather()
# print(y1.weight)
