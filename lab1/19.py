def cache(func):
    storage = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in storage:
            storage[key] = func(*args, **kwargs)
        return storage[key]
    return wrapper

@cache
def heavy_calculation(x, y):
    print(f"Выполняется реальное вычисление для {x} и {y}...")
    return x + y

print("Первый вызов функции:")
result_1 = heavy_calculation(5, 10)
print(f"Результат: {result_1}\n")

print("Второй вызов функции с теми же аргументами:")
result_2 = heavy_calculation(5, 10)
print(f"Результат из кэша: {result_2}\n")

print("Вызов функции с новыми аргументами:")
result_3 = heavy_calculation(10, 20)
print(f"Результат: {result_3}")
