vvod = input("Введите числа через пробел: ").split()
nums = []
for item in vvod:
    nums.append(float(item))
if len(nums) == 0:
    print("Вы ничего не ввели.")
else:
    uniq = []
    rep = []
    even = []
    odd = []
    neg = []
    floats = []
    sum5 = 0.0
    v_max = nums[0]
    v_min = nums[0]
    counts = {}
    for x in nums:
        if x in counts:
            counts[x] = counts[x] + 1
        else:
            counts[x] = 1
    for x in counts:
        if counts[x] == 1:
            uniq.append(x)
        else:
            rep.append(x)
    for x in nums:
        if x % 2 == 0:
            even.append(x)
        elif x % 2 == 1:
            odd.append(x)
        if x < 0:
            neg.append(x)
        if not x.is_integer():
            floats.append(x)
        if x % 5 == 0:
            sum5 = sum5 + x
        if x > v_max:
            v_max = x
        if x < v_min:
            v_min = x
    print("Результаты")
    print("1. Уникальные числа:", uniq)
    print("2. Повторяющиеся числа:", rep)
    print("3. Четные числа:", even)
    print("   Нечетные числа:", odd)
    print("4. Отрицательные числа:", neg)
    print("5. Числа с плавающей точкой:", floats)
    print("6. Сумма кратных 5:", sum5)
    print("7. Самое большое число:", v_max)
    print("8. Самое маленькое число:", v_min)
