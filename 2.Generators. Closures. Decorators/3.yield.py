print("Тут буде наш генератор")

# yield - для роботи генератора
def get_numbers():
    return [1,2,3]

print("default numbers", get_numbers())

# for ylik in get_numbers():
#     print("ylik", ylik)

def get_yield_numbers():
    yield 1
    yield 2
    yield 3

test1 = get_yield_numbers()
print("test1", test1)


print("---get_yield_numbers()---")
for item in get_yield_numbers():
    print(item, end='\t')

def my_counter_yield(n):
    i=0
    while i<=n:
        yield i
        i+=2

print()
for item in my_counter_yield(7):
    print(item, end = '\t')