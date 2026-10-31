text = input("Введите текст: ").lower()
for znak in [".", ",", "!", "?", "-", ":", ";"]:
    text = text.replace(znak, " ")
vse_slova = text.split()
print("Анализ всех слов")
vsego_1 = len(vse_slova)
print("Общее количество слов:", vsego_1)
if vsego_1 > 0:
    chastota_1 = {}
    samoe_chastoe_1 = vse_slova[0]
    maks_raz_1 = 0
    for slovo in vse_slova:
        if slovo in chastota_1:
            chastota_1[slovo] = chastota_1[slovo] + 1
        else:
            chastota_1[slovo] = 1
        if chastota_1[slovo] > maks_raz_1:
            maks_raz_1 = chastota_1[slovo]
            samoe_chastoe_1 = slovo
    print("Частота слов:", chastota_1)
    print("Самое частое слово:", samoe_chastoe_1, "(встречается", maks_raz_1, "раз)")
    samoe_korotkoe_1 = vse_slova[0]
    samoe_dlinnoe_1 = vse_slova[0]
    for slovo in vse_slova:
        if len(slovo) < len(samoe_korotkoe_1):
            samoe_korotkoe_1 = slovo
        if len(slovo) > len(samoe_dlinnoe_1):
            samoe_dlinnoe_1 = slovo
    print("Самое короткое слово:", samoe_korotkoe_1)
    print("Самое длинное слово:", samoe_dlinnoe_1)
else:
    print("Текст пустой.")
print("Анализ слов от 3-ех символов")
dlinnye_slova = []
for slovo in vse_slova:
    if len(slovo) >= 3:
        dlinnye_slova.append(slovo)
vsego_2 = len(dlinnye_slova)
print("Общее количество слов (от 3 символов):", vsego_2)
if vsego_2 > 0:
    chastota_2 = {}
    samoe_chastoe_2 = dlinnye_slova[0]
    maks_raz_2 = 0
    for slovo in dlinnye_slova:
        if slovo in chastota_2:
            chastota_2[slovo] = chastota_2[slovo] + 1
        else:
            chastota_2[slovo] = 1
        if chastota_2[slovo] > maks_raz_2:
            maks_raz_2 = chastota_2[slovo]
            samoe_chastoe_2 = slovo
    print("Частота слов:", chastota_2)
    print("Самое частое слово:", samoe_chastoe_2, "(встречается", maks_raz_2, "раз)")
    samoe_korotkoe_2 = dlinnye_slova[0]
    samoe_dlinnoe_2 = dlinnye_slova[0]
    for slovo in dlinnye_slova:
        if len(slovo) < len(samoe_korotkoe_2):
            samoe_korotkoe_2 = slovo
        if len(slovo) > len(samoe_dlinnoe_2):
            samoe_dlinnoe_2 = slovo
    print("Самое короткое слово:", samoe_korotkoe_2)
    print("Самое длинное слово:", samoe_dlinnoe_2)
else:
    print("Нет слов длиной от 3 символов.")
