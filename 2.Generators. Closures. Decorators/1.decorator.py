#print("Привіт! Тут будуть декоратори :)")

def my_decorator(func):
    def private_decorator():
        print("------My decorator-------")
        func()
        print("------End decoratory------")
    return private_decorator

@my_decorator
def hello_message():
    print("Привіт козаки! Хочу в Африку ):")

hello_message()