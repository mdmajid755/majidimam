class Animal:
    def speak(self):
        raise NotImplementedError()

class Dog(Animal):
    def speak(self):
        print("bark")

class Duck(Animal):
    def speak(self):
        print("Quack")


animals_list = [
    Dog(),Duck(),Dog()
]

for animal in animals_list:
    animal.speak()