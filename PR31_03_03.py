class MathOperations:

    @staticmethod
    def max_value(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min_value(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def avarage(a, b, c, d):
        return (a + b + c + d)/4

    @staticmethod
    def factorial(a):
        if a == 0:
            return 1
        else:
            result = 1
            for i in range(1, a + 1):
                result *= i
            return result

maximum = MathOperations.max_value(1, 2, 4, 3)
minimum = MathOperations.min_value(4, 2, 1, 3)
avarage = MathOperations.avarage(1, 2, 3, 4)
factorial = MathOperations.factorial(4)

print("Max: ", maximum)
print("Min: ", minimum)
print("Avg: ", avarage)
print("Factorial: ", factorial)