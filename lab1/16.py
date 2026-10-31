def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            sublist = lst.pop(i)
            flatten_list(sublist)
            for item in reversed(sublist):
                lst.insert(i, item)
        else:
            i += 1

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print(f"Исходный список: {list_a}")

flatten_list(list_a)
print(f"Модифицированный плоский список: {list_a}")
