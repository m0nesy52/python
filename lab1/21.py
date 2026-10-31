import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
        print(f"Функция {func.__name__} выполнилась за {execution_time:.3f} мс")
        return result
    return wrapper

@timing
def test_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

print("Запуск функции с замером времени:")
test_function()
