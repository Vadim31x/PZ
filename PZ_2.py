try:

    V1 = float(input("Введите скорость первого автомобиля (V1) в км/ч: "))
    V2 = float(input("Введите скорость второго автомобиля (V2) в км/ч: "))
    S = float(input("Введите начальное расстояние между автомобилями (S) в км: "))
    T = float(input("Введите время движения (T) в часах: "))

    if V1 < 0 or V2 < 0 or S < 0 or T < 0:
        print('Ошибка. значение не может быть отрицательным')
    else:
        sum_speed = V1 + V2
        total_distance_covered = sum_speed * T
        new_distance = abs(S - total_distance_covered)

        print(f"Расстояние между автомобилями через {T} часов: {new_distance:.2f} км")

except ValueError:
    print('Ошибка. Введено не число')
