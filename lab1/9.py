source_unit = input("Из какой единицы (мм, см, м, км, г, кг, т, сек, мин, час): ")
target_unit = input("В какую единицу (мм, см, м, км, г, кг, т, сек, мин, час): ")
value = float(input("Значение: "))

base_value = 0.0
if source_unit == "мм": 
    base_value = value / 1000
if source_unit == "см": 
    base_value = value / 100
if source_unit == "м":  
    base_value = value
if source_unit == "км": 
    base_value = value * 1000

if source_unit == "г":  
    base_value = value / 1000
if source_unit == "кг": 
    base_value = value
if source_unit == "т":  
    base_value = value * 1000

if source_unit == "сек": 
    base_value = value
if source_unit == "мин": 
    base_value = value * 60
if source_unit == "час": 
    base_value = value * 3600


result = 0.0

if target_unit == "мм": 
    result = base_value * 1000
if target_unit == "см": 
    result = base_value * 100
if target_unit == "м":  
    result = base_value
if target_unit == "км": 
    result = base_value / 1000

if target_unit == "г":  
    result = base_value * 1000
if target_unit == "кг": 
    result = base_value
if target_unit == "т":  
    result = base_value / 1000

if target_unit == "сек": 
    result = base_value
if target_unit == "мин": 
    result = base_value / 60
if target_unit == "час": 
    result = base_value / 3600

print("Результат:", round(result, 4), target_unit)
