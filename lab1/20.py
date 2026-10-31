def unique_elements(lst):
    flat_elements = []
    
    def extract_elements(item):
        if isinstance(item, list):
            for sub_item in item:
                extract_elements(sub_item)
        else:
            flat_elements.append(item)
            
    extract_elements(lst)
    
    unique_list = []
    for element in flat_elements:
        is_unique = True
        for unique_item in unique_list:
            if element == unique_item:
                is_unique = False
                break
        if is_unique:
            unique_list.append(element)
            
    return unique_list

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(f"Исходный вложенный список: {list_a}")

result = unique_elements(list_a)
print(f"Список уникальных элементов: {result}")
