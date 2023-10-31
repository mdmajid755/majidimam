class animal:
    name = "Animal"
    def speak(self):
        raise NotImplemented

class dog(animal):
    def speak(self):
        print("bark")

class duck(animal):
    def speak(self):
        print("quack")


myDog = dog()
myDuck = duck()
myAnimal = animal()
animals= [myDog, myDuck, myAnimal]

for pet in animals:
    print(pet.name)
    pet.speak()



