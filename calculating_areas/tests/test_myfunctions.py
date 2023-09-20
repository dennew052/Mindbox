from mypythonlib import myfunctions


def test_calculate_area():
    assert myfunctions.area_of_the_circle(0) == 'Данные некорректны'
    assert myfunctions.area_of_the_circle(1) == 3.14
    assert myfunctions.area_of_the_triangle(1, 2, 3) == 'Треугольник не существует'
    assert myfunctions.area_of_the_triangle(3, 4, 5) == 6.0
    assert myfunctions.area_of_the_triangle(3, 4, 6) == 5.33
    assert myfunctions.right_angled(3, 4, 5) == 'Треугольник является прямоугольным'
    assert myfunctions.right_angled(3, 4, 6) == 'Треугольник не является прямоугольным'
    assert myfunctions.right_angled(0, 0, 0) == 'Треугольник не существует'
    assert myfunctions.calculate_area(3) == "Фигуры не существует"
