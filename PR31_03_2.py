class AreaCalculator:
    calculation_count = 0

    @staticmethod
    def calculate_triangle_area(base, height):
        AreaCalculator.calculation_count += 1
        return 0.5 * base * height

    @staticmethod
    def calculate_rectangle_area(length, width):
        AreaCalculator.calculation_count += 1
        return length * width

    @staticmethod
    def calculate_square_area(side):
        AreaCalculator.calculation_count += 1
        return side ** 2

    @staticmethod
    def calculate_rhombus_area(diagonal1, diagonal2):
        AreaCalculator.calculation_count += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_calculation_count():
        return AreaCalculator.calculation_count

triangle_area = AreaCalculator.calculate_triangle_area(5, 8)
rectangle_area = AreaCalculator.calculate_rectangle_area(4, 6)
square_area = AreaCalculator.calculate_square_area(4)
rhombus_area = AreaCalculator.calculate_rhombus_area(6, 8)

print("Triangle:", triangle_area)
print("Rectangle:", rectangle_area)
print("Square:", square_area)
print("Rhombus:", rhombus_area)
print("Count: ", AreaCalculator.get_calculation_count())