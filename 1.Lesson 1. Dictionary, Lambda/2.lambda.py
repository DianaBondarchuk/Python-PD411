print("Тут будуть Лямбда вирази!")
# Лябда вирази - аналогічно, як у C#
#

mysquart = lambda x: x * x # буде підносити число до кавадрату
print(mysquart(5))

# Оголошення звичайної функції
def square(num):
    return num * num

print(square(5))

students = [
    {"name": "Bob", "age": 35},
    {"name": "Alice", "age": 18},
    {"name": "Bist", "age": 21},
]

# Мутація для сортування - змінюємо сам масив
#students.sort(key=lambda x: x["age"])
# students.sort(key=lambda x: x["age"])
# print(students)

sorted_stud = sorted(students, key=lambda student: student["age"])
print(sorted_stud)

print(type(students[0])) # вказуємо на консоль, який тип зберігається