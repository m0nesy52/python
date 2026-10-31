vvod1 = input("Введите первый набор чисел через пробел: ").split()
set1 = set()
for item in vvod1:
    set1.add(float(item))

vvod2 = input("Введите второй набор чисел через пробел: ").split()
set2 = set()
for item in vvod2:
    set2.add(float(item))

both = set1 & set2
only_first = set1 - set2
only_second = set2 - set1
exclusive = set1 ^ set2

print("\n--- Результаты ---")
print("1. Присутствуют в обоих одновременно:", list(both))
print("2. Из первого, которых нет во втором:", list(only_first))
print("   Из второго, которых нет в первом:", list(only_second))
print("3. Из обоих наборов, за исключением общих:", list(exclusive))
