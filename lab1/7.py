baza = 24.99
m = float(input("Минуты: "))
s = int(input("SMS: "))
mb = float(input("МБ: "))
doplata_m = 0.0
doplata_s = 0.0
doplata_mb = 0.0
if m > 60:
    doplata_m = (m - 60) * 0.89
if s > 30:
    doplata_s = (s - 30) * 0.59
if mb > 1024:
    doplata_mb = (mb - 1024) * 0.79
summa = baza + doplata_m + doplata_s + doplata_mb
nalog = summa * 0.02
itog = summa + nalog
print("Базовая сумма:", baza)
if doplata_m > 0:
    print("За минуты:", round(doplata_m, 2))
if doplata_s > 0:
    print("За SMS:", round(doplata_s, 2))
if doplata_mb > 0:
    print("За интернет:", round(doplata_mb, 2))
print("Налог:", round(nalog, 2))
print("Итого к оплате:", round(itog, 2))
