a = input("Введите пароль: ")
if len(a) < 16:
    print("Слишком короткий")
elif a.isdigit() or a.isalpha():
    print("Слабый пароль")
else:
    print("Надежный пароль")
