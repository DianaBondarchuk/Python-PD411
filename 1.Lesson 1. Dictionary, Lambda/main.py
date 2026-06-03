print("Привіт! Працюємо із словниками!")
# Dictionary - Це набері значень - де є ключ і значення
# Ключ не може повторитися

student = {
    "name": "Іван Марко",
    "age": 18,
    "grade": 95
}
# Значення словника
print(student)

print(student.get("name")) #Звертаємося по ключу
print(student["name"]) #Звертаємося по ключу

student["email"] = "ivan@gmail.com"
# Додали нове значення у словник
print(student)

del student["grade"] # Видаляємо оцінку
print(student)

# Перебір елементів словника
for key in student:
    print(f"{key}: {student[key]}")


