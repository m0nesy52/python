sum = float(input("Введите сумму покупки: "))
age = int(input("Введите возраст покупателя: "))
is_birthday = input("Сегодня день рождения? (да/нет): ").lower().strip() == "да"
is_vip = input("Клиент является VIP? (да/нет): ").lower().strip() == "да"
standard_discount = 0
vip_discount = 0
if sum > 1000:
    standard_discount += 10
if age >= 63:
    standard_discount += 5
if is_birthday:
    standard_discount += 5
if is_vip:
    vip_discount = 15
if vip_discount > standard_discount:
    final_discount_percent = vip_discount
else:
    final_discount_percent = standard_discount
if final_discount_percent > 25:
    final_discount_percent = 25
discount = sum * (final_discount_percent / 100)
total = sum - discount
print("Размер скидки:", final_discount_percent, "%")
print("Сумма скидки:", round(discount, 2), "руб.")
print("Итого к оплате:", round(total, 2), "руб.")
