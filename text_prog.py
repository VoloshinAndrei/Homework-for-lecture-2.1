class DomesticAnimals:
    weight = 10  # kg
    height = 50  # cm
    favorite_food = None

    def eat(self, value):
        self.weight += value


class Cows(DomesticAnimals):
    weight = 100  # kg
    height = 100  # cm

    def give_milk(self):
        print("You have cow's milk")
        self.weight -= 0.5


class Goats(DomesticAnimals):
    weight = 50  # kg

    def give_milk(self):
        print("You have goat's milk")
        self.weight -= 0.3


class Sheep(DomesticAnimals):
    weight = 50  # kg

    def give_wool(self):
        print("You have sheep's wool")
        self.weight -= 10


class Pigs(DomesticAnimals):
    weight = 70  # kg
    height = 30  # cm

    def kill_pig(self):
        print("You have pig's meat")
        self.weight = 0


class Ducks(DomesticAnimals):
    height = 30  # cm

    def kill_duck(self):
        print("You have duck's meat and feathers")
        self.weight = 0


class Chickens(DomesticAnimals):
    weight = 7
    height = 20  # cm

    def kill_chicken(self):
        print("You have chicken's meat and you can cook some chicken nuggets!")
        self.weight = 0

    def make_egg(self):
        print("You have chicken's egg")
        self.weight -= 0.1


class Geese(DomesticAnimals):
    weight = 15
    height = 20  # cm

    def save_rome(self):
        print("The geese have saved Rome!!!")
        self.weight += 1

    def give_feathers(self):
        print("You got some feathers and you can make a pen!")
        self.weight += 0.5


x1 = Cows()
print(x1.weight)
x1.give_milk()
print(x1.weight)

y1 = Geese()
y1.save_rome()
