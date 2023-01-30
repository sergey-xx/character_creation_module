"""Description of this programm."""


from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Проверяем на неотрицательность."""
    if your_number <= 0:
        return

    print("Мы вычислили квадратный корень из введённого вами числа.",
          f"Это будет: {CalculateSquareRoot(your_number)}")


print(message)
calc(25.5)
