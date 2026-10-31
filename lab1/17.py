def merge_dicts(dict_1, dict_2):
    for key, value in dict_2.items():
        if key in dict_1:
            if isinstance(dict_1[key], dict) and isinstance(value, dict):
                merge_dicts(dict_1[key], value)
            elif isinstance(dict_1[key], list) and isinstance(value, list):
                dict_1[key] = dict_1[key] + value
            elif isinstance(dict_1[key], set) and isinstance(value, set):
                dict_1[key] = dict_1[key] | value
            elif isinstance(dict_1[key], tuple) and isinstance(value, tuple):
                dict_1[key] = dict_1[key] + value
            else:
                dict_1[key] = value
        else:
            dict_1[key] = value

dict_a = {"a": 1, "b": {"c": 1, "f": 4}, "g":}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}, "g":}

print(f"Первый исходный словарь: {dict_a}")
print(f"Второй исходный словарь: {dict_b}")

merge_dicts(dict_a, dict_b)
print(f"Результат слияния с поддержкой вложенных коллекций: {dict_a}")
