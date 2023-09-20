# Mindbox
## Задание 1:
Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:
- Юнит-тесты
- Легкость добавления других фигур
- Вычисление площади фигуры без знания типа фигуры в compile-time
- Проверку на то, является ли треугольник прямоугольным
---
1. Файл с набором функций:\
[myfunctions.py](calculating_areas/myfunctions.py)

2. Юнит-тесты: \
[test_myfunctions.py](calculating_areas/tests/test_myfunctions.py)

3. Чтобы добавить новую фигуру, например квадрат, нужно:

   3.1 Открыть файл [myfunctions.py](calculating_areas/myfunctions.py)

   3.2 В функции start() на 64 строке добавить подсказку:
   ```
     3 - квадрат
   ```
   3.3 В функции calculate_area() на 54 строке добавить:
   ```
   elif num == 3:   
        a = float(input("Введите сторону квадрата: "))
        return area_of_the_square(a)
   ```
   3.4 Добавить новую функцию на строке 31:
   ```
   def area_of_the_square(a):
        if a > 0:
        return a ** 2
    else:
        return "Данные некорректны"
   ```
---
## Задание 2:
В датафреймах (pyspark.sql.DataFrame) заданы продукты, категории и связь между ними. Одному продукту может соответствовать много категорий, в одной категории может быть много продуктов. Напишите метод с помощью PySpark, который вернет все продукты с их категориями (датафрейм с набором всех пар «Имя продукта – Имя категории»). В результирующем датафрейме должны также присутствовать продукты, у которых нет категорий
___
1. Файл с PySpark DataFrame:\
[pyspark_dataframe.py](pyspark_dataframe/pyspark_dataframe.py)

