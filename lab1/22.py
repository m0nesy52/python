def type_check(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент на позиции {i} имеет тип {type(arg).__name__}, ожидался {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print("Вызов функции с корректными типами:")
result = add(5, 10)
print(f"Результат выполнения: {result}\n")

print("Вызов функции с некорректным типом (должно быть исключение):")
try:
    add(5, "10")
except TypeError as error:
    print(f"Перехвачено исключение: {error}")
