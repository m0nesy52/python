import random
a=random.randint(1,100)
num = int(input("Введите ваше число: "))
while num!=a:
    if (num > a):
        print("Меньше")
    if num < a:
        print("Больше")
    num = int(input("Введите ваше число: "))
print("Угадали")