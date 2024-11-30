"""
Составить функцию, которая выполнит суммирования числового ряда.
"""
while True:
    try:
        x = int(input("Введите послнднее число x: "))
        print(sum([i for i in range(1, x + 1)]))
    except ValueError:
        print("Ошибка")
    break
