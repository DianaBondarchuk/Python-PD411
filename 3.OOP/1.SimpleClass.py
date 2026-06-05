class Car:
    #this означає що цей метод належить даному класу
    #без this не працює
    def drive(this):
        print("Більше газу. Менше ям.")

bmw = Car()

bmw.drive()

class Animal:
    def speak(this):
        print("Даю голос")

class MiniPig(Animal):
    def speak(this):
        print("Хрю хрю ...")

class Dog(Animal):
    def speak(this):
        print("Гав гав ...")

pig = MiniPig()
pig.speak()

dog = Dog()
dog.speak()

# dog.show()

# Масив аномніх об'єктів
myAnimals = [MiniPig(), Dog()]

for obj in myAnimals:
    obj.speak()

def talk(obj):
    obj.speak() # Сюди передається вказівник на клас

talk(MiniPig())
talk(Dog())