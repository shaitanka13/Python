from rectangle1 import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print("Площадь 1 прямоугольника = ", rect_1.get_area())
print("Площадь 2 прямоугольника = ", rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print("Площадь 1 квадрата = ", square_1.get_area_square())
print("Площадь 2 квадрата = ", square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

circle_1 = Circle(5)
circle_2 = Circle(10)

print("Площадь 1 круга = ", circle_1.get_area_circle())
print("Площадь 2 круга = ", circle_2.get_area_circle())
