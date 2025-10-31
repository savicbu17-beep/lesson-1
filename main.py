# name = input("Введіть ваше ім'я: ")
# age = input("Введіть ваш вік: ")
# print(f"Привіт {name} тобі {age}")



# age = int(input("Введіть скільки вам років"))
# if age > 18:
#     print("Вхід дозволено")
# else:
#     print("Вхід заборонено")



# import random

# a = random.randint(1, 10)
# attempts = 3

# for i in range(attempts):
#     a = int(input("Вгадайте число від 1 до 10: "))
#     if a == number:
#         print("Вітаю! Ви вгадали!")
#         break
#     elif a < number:
#         print("Більше")
#     else:
#         print("Менше")
# else:
#     print(f"Гру завершено. Загадане число було {number}")



# p = int(input("Введіть число з: "))
# k = int(input("Введіть число по: "))

# for i in range(p, k + 1):
#     print(i, k=" ")



# n = int(input("Введіть число: "))
# faktorial = 1
# for i in range(1, n + 1):
#     faktorial *= i
# print(f"Факторіал числа {n} = {faktorial}")



# score = int(input("Введіть кількість балів: "))

# if 0 <= score <= 49:
#     print("Незадовільно")
# elif 50 <= score <= 69:
#     print("Задовільно")
# elif 70 <= score <= 89:
#     print("Добре")
# elif 90 <= score <= 99:
#     print("Відмінно")
# elif 99 <= score <= 100:
#     print("Ти геній")
# else:
#     print("Некоректна кількість балів")



a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
dia = input("Введіть дію: ")

if dia == "+":
    print(a + b)
elif dia == "-":
    print(a - b)
elif dia == "*":
    print(a * b)
elif dia == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print(a / b)
else:
    print("Невідома дія")
