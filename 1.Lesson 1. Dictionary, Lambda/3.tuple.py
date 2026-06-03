print("--Робота із кортеджами--")
myTuple = (23,12,34)
print("Набір даних у кортеджі")
print(myTuple)
print(type(myTuple))

print("Доступ до елементу")
print(myTuple[1])

try:
    myTuple[0] = 18 # У кортежі не можна змінювати елементи
except TypeError as e:
    print("Хюстон у нас проблеми:", e)

print(f"Кількість елементів у кортежі: {len(myTuple)}")

for item in myTuple:
    print("Елементи списку: ", item)

i=0
while(i<len(myTuple)):
    print(f"myTuple[{i}] = {myTuple[i]}")
    i += 1 # i++