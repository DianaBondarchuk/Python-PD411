def my_view_message(msg):
    message = msg[0:9] #Зрізаємо рядок
    # print("message", message)
    def private_fun():
        print(message)
    return private_fun #Повертаю вказіник на фукнцію

#Створюю вказівник на фукнцію, яка працює у середині
closure = my_view_message("Привіт козаки і козчки. Класна погода")
closure()