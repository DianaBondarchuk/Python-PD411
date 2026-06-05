class Student:

    # констркутор, але обов'язкова має приймати у себе self - this - без різниці
    def __init__(self, name):
        #name - То є public
        self.name = name
        self._age = 18 # Це змінна protected змінна
        self.__hobby = "Хобіт Хорсинг" # Це хобі приватна змінна
    # To String метод у Python це __str__ метод
    def __str__(self):
        return f"Student name = {self.name} age = {self._age} hobby = {self.__hobby}"
    
    def get_hobby(self):
        return self.__hobby

ivan = Student("Підкаблучник Василь")

print("name = ", ivan.name)
print("age = ", ivan._age)
print("hobby = ", ivan.get_hobby())
# print("hobby = ", ivan.__hobby) # Доступу до змінної не маємо
print(ivan) # Викликається метод __str__ автоматично
