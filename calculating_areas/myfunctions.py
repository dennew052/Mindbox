import math


def area_of_the_circle(radius):
    if radius <= 0:
        return "Данные некорректны"

    area = math.pi * radius ** 2
    return round(area, 2)


def area_of_the_triangle(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        return "Треугольник не существует"

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)


def right_angled(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        return "Треугольник не существует"

    if a > 0 and b > 0 and c > 0:
        if (a * a + b * b + c * c) - max(a, b, c) ** 2 == max(a, b, c) ** 2:
            return "Треугольник является прямоугольным"
        else:
            return "Треугольник не является прямоугольным"


def calculate_area(num):
    # 1 - circle, 2 - triangle

    if num == 1:
        radius = float(input("Введите радиус круга: "))
        return area_of_the_circle(radius)

    elif num == 2:
        a = float(input("Введите сторону A: "))
        b = float(input("Введите сторону B: "))
        c = float(input("Введите сторону C: "))
        num_action_triangle = int(input(f"""Какое действие вы хотите совершить?:
                1 - вычислить площадь треугольника
                2 - проверить, является ли треугольник прямоугольным

Выберите действие: """))
        if num_action_triangle == 1:
            return area_of_the_triangle(a, b, c)
        elif num_action_triangle == 2:
            return right_angled(a, b, c)
        else:
            return "Данные некорректны"

    else:
        return "Фигуры не существует"
        # raise Exception("Sorry, there is no figure with this number")


def start():
    num = int(input(f"""Существующие фигуры: 
        1 - круг 
        2 - треугольник 

Введите номер фигуры: """))

    answer = calculate_area(num)
    if type(answer) != str:
        print(f"Площадь: {answer}")
    else:
        print(answer)


if __name__ == '__main__':
    start()
