age = int(input("Возраст: "))
income = float(input("Ежемесячный доход: "))
amount = float(input("Сумма кредита: "))
months = int(input("Срок (в месяцах): "))
history = input("История (отличная/хорошая/удовлетворительная/плохая): ").lower().strip()
guarantor = input("Есть поручитель? (да/нет): ").lower().strip() == "да"
pledge = input("Есть залог? (да/нет): ").lower().strip() == "да"
month_pay = amount / months
ratio = (month_pay / income) * 100
risk = "Низкий"
rate = 12.0  # Базовая ставка
if ratio > 50 or history == "плохая" or age < 18 or age > 70:
    risk = "Критический"
    rate = 0.0
elif ratio > 35 or history == "удовлетворительная":
    risk = "Высокий"
    rate = 22.0
elif ratio > 20 or history == "хорошая":
    risk = "Средний"
    rate = 16.0
if risk == "Высокий" and (pledge or guarantor):
    risk = "Средний"
    rate = 16.0
elif risk == "Средний" and (pledge or guarantor):
    risk = "Низкий"
    rate = 12.0
if risk == "Критический":
    verdict = "ОТКЛОНИТЬ. Слишком высокие риски для банка."
elif risk == "Высокий":
    verdict = "ОДОБРИТЬ с условиями. Требуется повышенная ставка и жесткий контроль."
else:
    verdict = "ОДОБРИТЬ. Заемщик соответствует стандартам надежности."
print("Соотношение платежа к доходу в процентах:", ratio)
print("Категория риска:", risk)
if rate > 0:
    print("Предлагаемая процентная ставка:", rate)
else:
    print("Предлагаемая процентная ставка: кредит невозможен")
print("Рекомендация:", verdict)
